from enum import StrEnum

class ScopeType(StrEnum):
    HTTP = "HTTP"
    WEBTRANSPORT = "WEBTRANSPORT" # Reserved for future RCP versions

class HTTPRequestType(StrEnum):
    REQUEST = "HTTP.REQUEST"

class HTTPResponseType(StrEnum):
    START = "HTTP.RESPONSE.START"
    BODY = "HTTP.RESPONSE.BODY"
    TRAILERS = "HTTP.RESPONSE.TRAILERS"
    DISCONNECT = "HTTP.RESPONSE.DISCONNECT"
    DEBUG = "HTTP.RESPONSE.DEBUG"