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

LifespanReceiveEvents = (
    LifespanStartupEvent
    | LifespanShutdownEvent
)

LifespanSendEvents = (
    LifespanStartupCompleteEvent
    | LifespanStartupFailedEvent
    | LifespanShutdownCompleteEvent
    | LifespanShutdownFailedEvent
)

HTTPReceiveEvents = (
    HTTPRequestEvent
    | HTTPDisconnectEvent
)

HTTPSendEvents = (
    HTTPResponseStartEvent
    | HTTPResponseBodyEvent
    | HTTPResponseTrailersEvent
    | HTTPDisconnectEvent
    | HTTPResponseDebugEvent
)

RCPReceiveEvent = (
    HTTPReceiveEvents
    |LifespanReceiveEvents
)

RCPSendEvent = (
    HTTPSendEvents
    |LifespanSendEvents
)

RCPReceiveCallable = Callable[[], Awaitable[RCPReceiveEvent]]
RCPSendCallable = Callable[[RCPSendEvent], Awaitable[None]]

RCPApplication = Callable[
    [Scope, RCPReceiveCallable, RCPSendCallable]
    , Awaitable[None]
]
