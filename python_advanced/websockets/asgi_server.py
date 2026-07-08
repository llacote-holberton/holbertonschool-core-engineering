#!/usr/bin/env python3

# ===== APPLICATION related imports, using Starlette framework =====
# Required to set up app, the "orchestrator class".
from starlette.applications import Starlette
# Picking one kind of response among a collection of implementations
#   (PlainTextResponse, JSONResponse etc).
from starlette.responses import HTMLResponse
# Same concept, picking two implementations from a collection for routing.
from starlette.routing import Route, WebSocketRoute
# Additional imports for websocket transactions handling
# from websockets.exceptions import ConnectionClosed
from starlette.websockets import WebSocketDisconnect
# ===== SETTING UP LOGGING =====
import logging
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger('asgi_server')
logging.basicConfig(
    filename='asgi_server.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')


# ===== DEFINING THE WEB APP with dual modes HTTP/Websocket =====

LIVE_CONNECTIONS = set()

async def homepage(request):
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    await websocket.accept()
    LIVE_CONNECTIONS.add(websocket)

    try:
        while(True):
            # Writing for websocket library but Starlette is DIFFERENT!
            # msg_received = await websocket.recv()
            # echo = await websocket.send(msg_received)
            # from websockets.exceptions import ConnectionClosed
            # except ConnectionClosed
            msg_received = await websocket.receive_text()
            echo = await websocket.send_text(msg_received)

    except WebSocketDisconnect as ws_broken:
        log.debug("Connection closed for websocket %s", websocket)
    finally:
        # Better put here conceptually than in except.
        LIVE_CONNECTIONS.remove(websocket)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])


# ===== DEFINING THE ASGI Server to allow self_test =====
async def shortlife_uvicorn_run():
    """Function spawning a uvicorn server for only 20 seconds"""
    import uvicorn
    # 1. Server config
    server_lifespan = 20  # Seconds
    host = "0.0.0.0"
    port = 8000
    log_level = "debug"

    # uvicorn.run(app, port, log_level) CANNOT WORK for this use-case
    #   because it is blocking (synchronous)
    # We must explicitely use the "inner methods" of the framework.
    config = uvicorn.Config(
        app,
        host=host,
        port=port,
        log_level=log_level,
        log_config=None  # This deactivates internal log conf so will use mine
    )
    # Creating the server (not "started" yet)
    server = uvicorn.Server(config)

    # 2. Starting the "server listen" in a coroutine (non-blocking)
    server_task = asyncio.create_task(server.serve())

    # 3. Waiting for lifespan duration in seconds
    await asyncio.sleep(server_lifespan)

    # 4. Triggering "Graceful Shutdown" (to let existing connections close)
    log.info("Automatic shutdown...")
    server.should_exit = True

    # 5. Awaiting end of that task to ensure everything cleaned properly.
    await server_task



def sync_http_call(url):
    """
      Wrapper function for the blocking call into a synchronous function
      not only for readability but moreso because no other choice.
      Python accepts "anonymous functions" (lambda: xxx) but only a
        single expression is allowed.
      Yet our process requires multiple steps.
      And the run_in_executor which can be used to delegate this task
      to a sub-thread expects a function as parameter.
    """
    import urllib.request
    with urllib.request.urlopen(url) as response:
        return response.status, response.read().decode()


async def healthcheck__http_route(path_from_root: str = '/'):
    # DEADLOCK WARNING: urllib is synchronous -> freezes shared main thread.
    # It blocks the event loop -> Uvicorn cannot process this very request.
    # import urllib.request
    root_url = "http://127.0.0.1:8000"
    full_url = f"{root_url}{path_from_root}"
    log.debug("Full url to request to: %s", full_url)

    log.info("Starting Home HTTP endpoint check")
    try:
        loop = asyncio.get_running_loop()
        status, html_content = await loop.run_in_executor(
            None,            # Custom executor (None -> default behaviour)
            sync_http_call,  # Function to execute in subthread
            full_url              # Parameter(s) for the function, N params = N args
        )
        log.info(f"[TEST HTTP] Status: {status}")
        log.info(f"Content: {html_content}")
    except Exception as e:
        log.error(f"[TEST HTTP] Failure: {e}")


async def healthcheck__websocket_route(endpoint: str = '/ws'):
    from websockets.asyncio.client import connect as ws_connect
    log.info("Starting Basic Websocket endpoint check")
    root_url = "ws://127.0.0.1:8000"

    # Bad practice to have "implicit import made at parent level"
    #   but acceptable here I just want something quick.
    async with ws_connect(f"{root_url}{endpoint}") as client_mockup:
        test_message = "This message should be echoed from server"
        await client_mockup.send(test_message)
        received_answer = await client_mockup.recv()
        if received_answer == test_message:
            log.info("Ws endpoints works")
        else:
            log.error("WS endpoint does not work as intended")


async def healthchecks():

    log.info("Running basic healthchecks for HTTP and WS endpoints")
    await healthcheck__http_route('/')
    await healthcheck__websocket_route('/ws')


async def app_self_contained_test():
    # THIS cannot work because that call just creates a Coroutine but does
    # NOT add it to the asynchronous execution task stack.
    # shortlife_uvicorn_run()
    # THIS would technically work but because we have "built-in timed life"
    #   awaiting it would mean we "sleep" and "healthchecks" once the server
    #   has already shut down.
    # await shortlife_uvicorn_run()
    # SO the ONLY WAY to have something working as intended is to
    #   explicitely create an asynchronous task which will be started ASAP.
    server_task = asyncio.create_task(shortlife_uvicorn_run())
    await asyncio.sleep(2)
    await healthchecks()
    # And as usual we wait for the end of our server task to ensure clean end.
    await server_task

if __name__ == "__main__":
    import asyncio
    asyncio.run(app_self_contained_test())


# ========== INSTRUCTIONS =========
# Implement an application which...
# Serves an HTML page at http://localhost:8000
# AND exposes a Websocket endpoint at ws://localhost:8000/ws
# * Accepting websocket connections on that endpoint to "echo"
#   any message received back to the sender client, optionally
#   keeping a list of connected clients in case of (why not).

# ========== BRAINSTORM ==========
# Uvicorn is the "orchestrator", the "interface exposed to the web".
# It is tasked with receiving HTTP or Websocket requests, check if
#   there is an app suited to handle them, case arising propagating to them
#   then pushing back the generated response to the client.

# Starlette is a framework facilitating the creation of the apps
#   in a way that respects logic and protocols expected by
#   ASGI-compliant servers so you can just "plug and play" one in the other.
# You define the urls it can answer to by creating and managing a List of
#   Objects which all duck-type the Route related attributes and methods
# Route class and subclasses are instanciated with at least two
#     positional arguments: 'path' and 'handler'.
# You can provide them at app creation by giving named argument 'routes'

# === Notes on 'host' parameter ===
# 127.0.0.1 is a "special IP" which is interpreted by programs as
#   "only requests coming from the same machine" (the "local loopback").
# 0.0.0.0   is a "special IP" which is interpreted by programs as
#   "listen from everywhere" (every network interfaces)
#   which will allow third-party even from internet to access it.
