# Websockets Project - Task 05 ASGI Integration

## Introduction

In this step, you will integrate WebSocket communication into a web-facing Python application.

Until now, your servers have been started using simple helper functions designed for development and experimentation. These approaches are useful for learning, but they are not suitable for real-world applications.

In production environments, applications must:

* Handle different types of traffic (HTTP and WebSocket)
* Support multiple simultaneous users
* Be scalable and maintainable
* Run behind a dedicated application server

To achieve this, Python web applications use standardized interfaces such as **WSGI** and **ASGI**.

* **WSGI (Web Server Gateway Interface)** is designed for traditional synchronous HTTP applications.
* **ASGI (Asynchronous Server Gateway Interface)** extends this model to support asynchronous communication and long-lived connections such as WebSockets.

ASGI is required in this project because:

* WebSockets rely on persistent connections
* Multiple clients must be handled concurrently
* The application must support both HTTP (for serving pages) and WebSocket communication

While it is possible to implement an ASGI application directly, it would require handling low-level details such as routing, connection management, and protocol handling.

Frameworks like **Starlette** provide a higher-level abstraction that simplifies this process. They allow you to:

* Define HTTP and WebSocket routes clearly
* Focus on application logic instead of protocol details
* Reduce boilerplate code
* Follow patterns commonly used in real-world applications

Using a framework in this step is intentional: it reflects how production systems are built, where developers rely on well-tested tools to manage infrastructure concerns while focusing on business logic.

In this step, you will build an ASGI application using **Starlette**, and run it using **Uvicorn**, a production-ready ASGI server.

This setup reflects how real-world applications are structured and deployed.

---

## Resources

* [https://asgi.readthedocs.io/en/latest/introduction.html](/rltoken/ylE9yjuenDRdMEHeLdobTg)
* [https://www.starlette.io/](/rltoken/7JU1685r-euIrpGxCCnr1w)
* [https://www.starlette.io/websockets/](/rltoken/bjC_GaGC2fWLDfyKhZsDCg)
* [https://www.uvicorn.org/](/rltoken/xsu0Zwp9vrdzI5v-ztariQ)

---

## Instructions

Implement an application that:

* Serves an HTML page at:

```text
http://localhost:8000
```

* Exposes a WebSocket endpoint at:

```text
ws://localhost:8000/ws
```

* Accepts WebSocket connections on `/ws`
* Receives text messages from connected clients
* Sends back the exact same message to the sender (echo behavior)

---

## Expected Behavior

When accessing:

```text
http://localhost:8000
```

A web page must be returned.

When connecting to:

```text
ws://localhost:8000/ws
```

and sending:

```text
Hello
```

The server must respond:

```text
Hello
```

---

## Constraints

* Use an ASGI-compatible application
* Use **Starlette** for routing
* The application must handle both HTTP and WebSocket connections
* The WebSocket endpoint must be `/ws`
* The WebSocket behavior must follow echo logic
* The application must listen on port `8000`

---

## Running the Application

You must run the application using **Uvicorn**:

```bash
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

### Explanation of parameters

* `asgi_server:app`
  Refers to the Python file and application instance:

  * `asgi_server` → file name (`asgi_server.py`)
  * `app` → ASGI application object inside the file

* `--host 0.0.0.0`
  Makes the server accessible from outside the local machine (useful for testing and containers)

* `--port 8000`
  Specifies the port where the server will run

* `--reload`
  Automatically restarts the server when code changes (development only)

---

## Suggested Approach

* Create a Starlette application
* Define:

    * one HTTP route (`/`)
    * one WebSocket route (`/ws`)
* Accept the WebSocket connection before receiving messages
* Use a loop to receive and send messages continuously
* Keep the connection open for multiple exchanges

Example structure:

```python
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute

async def homepage(request):
    return HTMLResponse(&quot;&lt;h1&gt;WebSocket App&lt;/h1&gt;&quot;)

async def websocket_endpoint(websocket):
    await websocket.accept()
    # message loop here

app = Starlette(routes=[
    Route(&quot;/&quot;, homepage),
    WebSocketRoute(&quot;/ws&quot;, websocket_endpoint),
])
```
