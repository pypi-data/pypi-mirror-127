from typing import List, Optional

from pyflp.event import _DataEventType
from pyflp.plugin.plugin import _EffectPlugin


class FNoteBook2(_EffectPlugin):
    """Implements Fruity Notebook 2.

    [Manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20NoteBook%202.htm)
    """

    # 0,0,0,0 4b
    # active page number 4b
    # page number 4b - (data length / 2) varint - text in utf16 for each page
    # 255, 255, 255, 255 4b
    # Editing enabled or disabled 1b

    def __repr__(self) -> str:
        return "<Fruity Notebook 2 {}, {}, {}>".format(
            f"{len(self.pages)} pages",
            f"active_page_number={self.active_page}",
            f"editable={self.editable}",
        )

    # * Properties
    @property
    def pages(self) -> List[str]:
        """List of strings. One string per page."""
        return getattr(self, "_pages", [])

    @pages.setter
    def pages(self, value: List[str]):
        self._r.seek(8)
        for page_num, page in enumerate(value):
            self._r.write_I(page_num)  # TODO: or page_num + 1?
            wstr = page.encode("utf-16", errors="ignore")
            self._r.write_v(len(wstr))
            self._r.write(wstr)  # NULL bytes are not appended at the end
        self._pages = value

    @property
    def active_page(self) -> Optional[int]:
        """Currently selected page number."""
        return getattr(self, "_active_page", None)

    @active_page.setter
    def active_page(self, value: int):
        assert value in range(1, len(self._pages) + 1)  # TODO
        self._r.seek(4)
        self._r.write_I(value)
        super()._setprop("active_page", value)

    @property
    def editable(self) -> Optional[bool]:
        """Whether notebook is editable or read-only."""
        return getattr(self, "_editable", None)

    @editable.setter
    def editable(self, value: bool):
        self._r.seek(-1, 2)
        self._r.write_bool(value)
        super()._setprop("editable", value)

    def _parse_data_event(self, e: _DataEventType) -> None:
        super()._parse_data_event(e)
        r = self._r
        r.seek(4)
        self._active_page = r.read_I()
        while True:
            page_num = r.read_i()
            if page_num == -1:
                break
            size = r.read_v()
            buffer = r.read(size * 2)
            self._pages.append(buffer.decode("utf-16", errors="ignore"))
        self._editable = r.read_bool()

    def __init__(self):
        self._pages = []
        super().__init__()
