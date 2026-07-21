from enum import StrEnum
    
# Scope types used when creating a new scope.
class ScopeType(StrEnum):
    HTTP = "HTTP"
    LIFESPAN = "LIFESPAN"
    
    # Reserved for future RCP versions
    WEBTRANSPORT = "WEBTRANSPORT"

# HTTP events sent after the HTTP scope is created.
class HTTPConnectionEventType(StrEnum):
    REQUEST = "HTTP.REQUEST"
    DISCONNECT = "HTTP.DISCONNECT"

# HTTP response event types.
class HTTPResponseEventType(StrEnum):
    START = "HTTP.RESPONSE.START"
    BODY = "HTTP.RESPONSE.BODY"
    TRAILERS = "HTTP.RESPONSE.TRAILERS"
    DEBUG = "HTTP.RESPONSE.DEBUG"

# Lifespan event types.
class LifespanEventType(StrEnum):
    STARTUP = "LIFESPAN.STARTUP"
    SHUTDOWN = "LIFESPAN.SHUTDOWN"
    STARTUP_COMPLETE = "LIFESPAN.STARTUP.COMPLETE"
    STARTUP_FAILED = "LIFESPAN.STARTUP.FAILED"
    SHUTDOWN_COMPLETE = "LIFESPAN.SHUTDOWN.COMPLETE"
    SHUTDOWN_FAILED = "LIFESPAN.SHUTDOWN.FAILED"

# HTTP protocol versions used by RCP.
class HTTPVersions(StrEnum):
    HTTP3 = "3"