import enum
from typing import Any, Optional

from bytesioex import BytesIOEx

from pyflp.event import DataEvent
from pyflp.flobject import _FLObject
from pyflp.properties import _EnumProperty


@enum.unique
class InsertFlags(enum.IntFlag):
    """Used by `InsertParametersEvent.flags`."""

    None_ = 0
    ReversePolarity = 1 << 0
    """Phase is inverted."""

    SwapLeftRight = 1 << 1
    """Left and right channels are swapped."""

    EnableEffects = 1 << 2
    """All slots are enabled. If this flag is absent, slots are bypassed."""

    Enabled = 1 << 3
    """Insert is in enabled state."""

    DisableThreadedProcessing = 1 << 4
    U5 = 1 << 5
    DockMiddle = 1 << 6
    """Layout -> Dock to -> Middle."""

    DockRight = 1 << 7
    """Layout -> Dock to -> Right."""

    U8 = 1 << 8
    U9 = 1 << 9
    ShowSeparator = 1 << 10
    """A separator is shown to the left of the insert."""

    Locked = 1 << 11
    """Insert is in locked state."""

    Solo = 1 << 12
    """Insert is the only active insert throught the mixer i.e soloed."""

    U13 = 1 << 13
    U14 = 1 << 14
    AudioTrack = 1 << 15
    """Whether insert is linked to an audio track."""


class InsertParametersEvent(DataEvent):
    """Implements `Insert.EventID.Parameters`."""

    _chunk_size = 12

    def __init__(self, data: bytes):
        from pyflp.insert.insert import Insert

        super().__init__(Insert.EventID.Parameters, data)
        self.__r = r = BytesIOEx(data)
        self.u1 = r.read_I()
        self.flags = InsertFlags(r.read_I())
        self.u2 = r.read_I()

    def __repr__(self) -> str:
        return f"<InsertParametersEvent flags={self.flags}, u1={self.u1}, u2={self.u2}>"

    def set(self, n: str, v: int):
        r = self.__r
        if n == "u1":
            r.seek(0)
            r.write_I(v)
        elif n == "flags":
            r.seek(4)
            r.write_I(v)
        elif n == "u2":
            r.seek(8)
            r.write_I(v)
        r.seek(0)
        self.dump(r.read())


class InsertParameters(_FLObject):
    """Used by `Insert.flags`, `Insert.enabled` and `Insert.locked`."""

    def _setprop(self, n: str, v: Any):
        self.__ipe.set(n, v)
        super()._setprop(n, v)

    flags: Optional[InsertFlags] = _EnumProperty(InsertFlags)

    def _parse_data_event(self, e: InsertParametersEvent) -> None:
        self.__ipe = self._events["polyphony"] = e
        self._flags = e.flags
