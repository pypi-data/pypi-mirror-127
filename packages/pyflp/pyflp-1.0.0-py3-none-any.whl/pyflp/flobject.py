import abc
import enum
from typing import Any, Dict, Optional, ValuesView

from pyflp.constants import DATA_TEXT_EVENTS, BYTE, DWORD, TEXT, DATA, WORD
from pyflp.event import (
    _EventType,
    ByteEvent,
    WordEvent,
    DWordEvent,
    _DWordEventType,
    ColorEvent,
    TextEvent,
    _DataEventType,
)
from pyflp.properties import _Property
from pyflp.utils import FLVersion


class _FLObject(abc.ABC):
    """Abstract base class for the FLP object model."""

    _count = 0

    # Set by Parser and can be modified by Misc.version
    fl_version: Optional[FLVersion] = None

    @enum.unique
    class EventID(enum.IntEnum):
        """Stores event IDs used by `parse_event` delegates."""

    def __repr__(self) -> str:
        reprs = []
        for k in vars(type(self)).keys():
            prop = getattr(type(self), k)
            attr = getattr(self, k)
            if isinstance(prop, _Property):
                reprs.append(f"{k}={attr!r}")
        return f"<{type(self).__name__} {', '.join(reprs)}>"

    def _setprop(self, n, v):
        """Dumps a property value to the underlying event
        provided `_events` has a key with name `n`."""

        ev = self._events.get(n)
        if ev is not None:
            ev.dump(v)

    # * Parsing logic
    def parse_event(self, event: _EventType) -> None:
        """Adds and parses an event from the event store.

        Note: Delegates
            Uses delegate methods `_parse_byte_event`, `_parse_word_event`,
            `_parse_dword_event`, `_parse_text_event` and `_parse_data_event`.

        Tip: Overriding
            Can be overriden when a derived class contains properties
            holding `FLObject` derived classes, *for e.g.* `Insert.slots` holds
            `List[InsertSlot]` and whenever the event ID belongs to
            `InsertSlot.EventID`, it is passed to the slot's `parse_event`
            method directly.

        Args:
            event (Event): Event to dispatch to `self._parseprop`."""

        # Convert event.id from an int to a member of the class event ID
        try:
            event.id = self.EventID(event.id)
        except ValueError:
            # The delegates below should assign the proper value
            pass

        id = event.id

        if id >= BYTE and id < WORD:
            self._parse_byte_event(event)
        elif id >= WORD and id < DWORD:
            self._parse_word_event(event)
        elif id >= DWORD and id < TEXT:
            self._parse_dword_event(event)
        elif (id >= TEXT and id < DATA) or id in DATA_TEXT_EVENTS:
            self._parse_text_event(event)
        else:
            self._parse_data_event(event)

    def _parse_byte_event(self, _: ByteEvent) -> None:
        pass

    def _parse_word_event(self, _: WordEvent) -> None:
        pass

    def _parse_dword_event(self, _: _DWordEventType) -> None:
        pass

    def _parse_text_event(self, _: TextEvent) -> None:
        pass

    def _parse_data_event(self, _: _DataEventType) -> None:
        pass

    # * Property parsing logic
    def _parseprop(self, event: _EventType, key: str, value: Any):
        """Reduces boilerplate for `parse_event()` delegate methods.
        Not to be used unless helper `_parse_*` methods aren't useful."""

        self._events[key] = event
        setattr(self, "_" + key, value)

    def _parse_bool(self, event: ByteEvent, key: str):
        """`self._parseprop` for boolean properties."""
        self._parseprop(event, key, event.to_bool())

    def _parse_B(self, event: ByteEvent, key: str):
        """`self._parseprop` for uint8 properties."""
        self._parseprop(event, key, event.to_uint8())

    def _parse_b(self, event: ByteEvent, key: str):
        """`self._parseprop` for int8 properties."""
        self._parseprop(event, key, event.to_int8())

    def _parse_H(self, event: WordEvent, key: str):
        """`self._parseprop` for uint16 properties."""
        self._parseprop(event, key, event.to_uint16())

    def _parse_h(self, event: WordEvent, key: str):
        """`self._parseprop` for int16 properties."""
        self._parseprop(event, key, event.to_int16())

    def _parse_I(self, event: DWordEvent, key: str):
        """`self._parseprop` for uint32 properties."""
        self._parseprop(event, key, event.to_uint32())

    def _parse_i(self, event: DWordEvent, key: str):
        """`self._parseprop` for int32 properties."""
        self._parseprop(event, key, event.to_int32())

    def _parse_s(self, event: TextEvent, key: str):
        """`self._parseprop` for string properties."""
        self._parseprop(event, key, event.to_str())

    def _parse_color(self, event: ColorEvent, key: str = "color"):
        """`self._parseprop` for Color properties."""
        self._parseprop(event, key, event.to_color())

    def _parse_flobject(self, event: _EventType, key: str, value: Any):
        """`self._parseprop` for `FLObject` properties. e.g `Channel.delay`
        is of type `ChannelDelay` which is itself an `FLObject` subclass.

        This method works only for classes which work on a single event
        and occur once inside the container class!"""

        if not hasattr(self, "_" + key):
            assert isinstance(value, _FLObject)
            self._parseprop(event, key, value)
        obj: _FLObject = getattr(self, "_" + key)
        obj.parse_event(event)

    def _save(self) -> ValuesView[_EventType]:
        """Returns the events stored in `self._events` as a read only view."""
        return self._events.values()

    def __init__(self):
        cls = type(self)
        self._idx = cls._count
        cls._count += 1
        self._events: Dict[str, _EventType] = {}
        super().__init__()
