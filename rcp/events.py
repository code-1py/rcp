from __future__ import annotations

from .types import HTTPConnectionEventType, HTTPResponseEventType, ScopeType, HTTPVersions
from .methods import RequestMethod
from typing import NotRequired ,Any, Literal, TypedDict
from collections.abc import Iterable
from .rcp import RCP
from .scheme import HTTPScheme

Headers = Iterable[tuple[bytes, bytes]]

# HTTP events
class HTTPRequestEvent(TypedDict):
    type: Literal[HTTPConnectionEventType.REQUEST]
    body: bytes
    more_body: bool

class HTTPResponseDebugEvent(TypedDict):
    type: Literal[HTTPResponseEventType.DEBUG]
    info: dict[str, object]

class HTTPResponseStartEvent(TypedDict):
    type: Literal[HTTPResponseEventType.START]
    status: int
    headers: NotRequired[Headers]
    trailers: NotRequired[bool]


class HTTPResponseBodyEvent(TypedDict):
    type: Literal[HTTPResponseEventType.BODY]
    body: bytes
    more_body: NotRequired[bool]


class HTTPResponseTrailersEvent(TypedDict):
    type: Literal[HTTPResponseEventType.TRAILERS]
    headers: Headers
    more_trailers: bool


class HTTPDisconnectEvent(TypedDict):
    type: Literal[HTTPConnectionEventType.DISCONNECT]