from .events import (
    HTTPRequestEvent,
    HTTPResponseDebugEvent,
    HTTPResponseStartEvent,
    HTTPResponseBodyEvent,
    HTTPResponseTrailersEvent,
    HTTPDisconnectEvent,
    LifespanStartupEvent,
    LifespanShutdownEvent,
    LifespanStartupCompleteEvent,
    LifespanStartupFailedEvent,
    LifespanShutdownCompleteEvent,
    LifespanShutdownFailedEvent
)
from .scopes import (
    HTTPScope,
    LifespanScope
)
from collections.abc import Callable, Awaitable

Scope = HTTPScope | LifespanScope

RCPReceiveEvent = (
    HTTPRequestEvent
    | HTTPDisconnectEvent
    | LifespanStartupEvent
    | LifespanShutdownEvent
)

RCPSendEvent = (
    HTTPResponseStartEvent
    | HTTPResponseBodyEvent
    | HTTPResponseTrailersEvent
    | HTTPDisconnectEvent
    | LifespanStartupCompleteEvent
    | LifespanStartupFailedEvent
    | LifespanShutdownCompleteEvent
    | LifespanShutdownFailedEvent
    | HTTPResponseDebugEvent
)

RCPReceiveCallable = Callable[[], Awaitable[RCPReceiveEvent]]
RCPSendCallable = Callable[[RCPSendEvent], Awaitable[None]]

RCPApplication = Callable[
    [Scope, RCPReceiveCallable, RCPSendCallable]
    , Awaitable[None]
]
