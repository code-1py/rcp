from __future__ import annotations

from .types import HTTPConnectionEventType, HTTPResponseEventType, ScopeType, HTTPVersions ,LifespanEventType
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

class LifespanStartupEvent(TypedDict):
    type: Literal[LifespanEventType.STARTUP]


class LifespanShutdownEvent(TypedDict):
    type: Literal[LifespanEventType.SHUTDOWN]


class LifespanStartupCompleteEvent(TypedDict):
    type: Literal[LifespanEventType.STARTUP_COMPLETE]


class LifespanStartupFailedEvent(TypedDict):
    type: Literal[LifespanEventType.STARTUP_FAILED]
    message: str


class LifespanShutdownCompleteEvent(TypedDict):
    type: Literal[LifespanEventType.SHUTDOWN_COMPLETE]


class LifespanShutdownFailedEvent(TypedDict):
    type: Literal[LifespanEventType.SHUTDOWN_FAILED]
    message: str