# Rivora Contract Protocol (RCP)

RCP (Rivora Contract Protocol) is a lightweight interface specification that defines how applications, frameworks, and servers communicate within the Rivora ecosystem.

RCP provides a contract between frameworks and servers while remaining independent of any specific implementation.

Version 1.0 is designed for HTTP/3 and QUIC-based servers.

## Repository

[GitHub Repository](https://github.com/code-1py/rcp)

---

# Architecture

RCP sits between a framework and a server.

```text
Application
     ↓
 Framework
     ↓
    RCP
     ↓
   Server
     ↓
HTTP/3 / QUIC
```

A typical request flow is:

```text
Client
    ↓
 Server
    ↓
 Creates Scope
    ↓
 Calls Application
    ↓
 Application receives Events
    ↓
 Application sends Events
    ↓
 Server sends Response
```

---

# Design Goals

* HTTP/3-first architecture
* Strong typing
* Minimal interface
* Framework and server separation
* Support for streaming
* Support for lifespan events
* Forward compatibility through extensions
* Future WebTransport support

---

# Installation

```bash
pip install rivora-rcp
```

---

# Core Concepts

RCP is built around three objects:

* Scope
* Receive
* Send

An application receives these objects from the server.

```python
async def app(scope, receive, send):
    ...
```

---

# Application Interface

Applications must follow the RCP application contract.

```python
RCPApplication = Callable[
    [Scope, RCPReceiveCallable, RCPSendCallable],
    Awaitable[None]
]
```

Example:

```python
async def app(scope, receive, send):
    ...
```

## Parameters

### scope

Contains metadata describing the connection.

### receive

Receives events from the server.

```python
event = await receive()
```

### send

Sends events to the server.

```python
await send(event)
```

---

# Scopes

A scope contains information known when the connection is created.

## HTTP Scope

```python
class HTTPScope(TypedDict):
    type: Literal[ScopeType.HTTP]
    rcp: RCP

    http_version: HTTPVersions

    method: RequestMethod
    scheme: HTTPScheme

    path: str
    raw_path: bytes
    query_string: bytes
    root_path: str

    headers: Headers

    client: tuple[str, int] | None
    server: tuple[str, int | None] | None

    state: NotRequired[dict[str, Any]]
    extensions: NotRequired[dict[str, dict[object, object]]]
```

### Fields

| Field        | Description                    |
| ------------ | ------------------------------ |
| type         | Scope type                     |
| rcp          | RCP version information        |
| http_version | HTTP protocol version          |
| method       | Request method                 |
| scheme       | Request scheme                 |
| path         | Decoded request path           |
| raw_path     | Original path bytes            |
| query_string | Raw query string               |
| root_path    | Mounted root path              |
| headers      | Request headers                |
| client       | Client address and port        |
| server       | Server address and port        |
| state        | Shared request state           |
| extensions   | Optional protocol capabilities |

---

## Lifespan Scope

```python
class LifespanScope(TypedDict):
    type: Literal[ScopeType.LIFESPAN]
    rcp: RCP

    state: NotRequired[dict[str, Any]]
```

Used during application startup and shutdown.

---

# HTTP Events

## HTTPRequestEvent

Sent by the server to the application.

```python
{
    "type": HTTPConnectionEventType.REQUEST,
    "body": b"...",
    "more_body": False
}
```

### Fields

| Field     | Description                     |
| --------- | ------------------------------- |
| type      | Event type                      |
| body      | Request body chunk              |
| more_body | Additional body chunks expected |

---

## HTTPResponseStartEvent

Sent by the application to the server.

```python
{
    "type": HTTPResponseEventType.START,
    "status": 200
}
```

### Fields

| Field    | Description                     |
| -------- | ------------------------------- |
| type     | Event type                      |
| status   | HTTP response status            |
| headers  | Response headers                |
| trailers | Indicates trailers will be sent |

---

## HTTPResponseBodyEvent

```python
{
    "type": HTTPResponseEventType.BODY,
    "body": b"Hello",
    "more_body": False
}
```

### Fields

| Field     | Description                |
| --------- | -------------------------- |
| type      | Event type                 |
| body      | Response body chunk        |
| more_body | Additional chunks expected |

---

## HTTPResponseTrailersEvent

```python
{
    "type": HTTPResponseEventType.TRAILERS,
    "headers": [...],
    "more_trailers": False
}
```

Used to send HTTP trailers after the response body.

---

## HTTPResponseDebugEvent

```python
{
    "type": HTTPResponseEventType.DEBUG,
    "info": {}
}
```

Optional debugging information.

Servers may ignore this event.

---

## HTTPDisconnectEvent

```python
{
    "type": HTTPConnectionEventType.DISCONNECT
}
```

### Receive

Indicates that the client disconnected.

### Send

Requests immediate connection termination.

When sent by the application, the server should close the connection without sending additional events.

---

# Lifespan Events

Lifespan events are used to manage application startup and shutdown.

## Startup

Server:

```python
{
    "type": LifespanEventType.STARTUP
}
```

Application:

```python
{
    "type": LifespanEventType.STARTUP_COMPLETE
}
```

or

```python
{
    "type": LifespanEventType.STARTUP_FAILED,
    "message": "Reason"
}
```

---

## Shutdown

Server:

```python
{
    "type": LifespanEventType.SHUTDOWN
}
```

Application:

```python
{
    "type": LifespanEventType.SHUTDOWN_COMPLETE
}
```

or

```python
{
    "type": LifespanEventType.SHUTDOWN_FAILED,
    "message": "Reason"
}
```

---

# Example Application

```python
from rcp import (
    HTTPResponseEventType,
)

async def app(scope, receive, send):
    await send(
        {
            "type": HTTPResponseEventType.START,
            "status": 200,
        }
    )

    await send(
        {
            "type": HTTPResponseEventType.BODY,
            "body": b"Hello from RCP",
        }
    )
```

---

# Version Information

## RCP 1.0

Supported:

* HTTP/3
* QUIC
* Typed scopes
* Typed events
* Lifespan protocol

Reserved for future versions:

* WebTransport
* HTTP/2 support
* HTTP/1.1 support
* Additional protocol extensions

---

# License

RCP is licensed under the MIT License.

See the LICENSE file for details.
