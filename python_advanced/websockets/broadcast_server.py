#!/usr/bin/env python3

"""Echo server using the asyncio API."""

# ===== IMPORTS FOR FUNCTIONAL BEHAVIOUR =====
# Required to handle asynchronous tasks (imperative for websockets library)
import asyncio
# Using the provided "websockets-based server" from websockets library.
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed
from websockets.asyncio.server import broadcast

# Used to generate unique ids easily.

# ===== SETTING UP LOGGING =====
import logging
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger('broadcast_server')
logging.basicConfig(
    filename='broadcast_server.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

# ===== SERVER FUNCTIONAL BEHAVIOUR =====
# Set to store active connections.
CONNECTIONS_REGISTRY = set()
CAST_MODE = 'broadcast'


async def connection_handler(websocket):
    """Creates a websocket handler to send validation on message received"""
    debug_msg_tmpl = "ws %s %s, new registry state: %s"
    try:
        log.debug("New connection received!")
        CONNECTIONS_REGISTRY.add(websocket)
        log.debug(debug_msg_tmpl, websocket, 'added', CONNECTIONS_REGISTRY)
        while (True):
            msg_received = await websocket.recv()
            trimmed = msg_received.strip()
            valid = isinstance(trimmed, str) and len(trimmed) > 0

            if valid and CAST_MODE == 'unicast':
                await websocket.send(f"U:{trimmed}")

            elif valid and CAST_MODE == 'broadcast':
                broadcast(CONNECTIONS_REGISTRY, f"B:{trimmed}")

            else:
                await websocket.send("ERR:EMPTY")

    except ConnectionClosed as cc:
        CONNECTIONS_REGISTRY.discard(websocket)
        log.debug(debug_msg_tmpl, websocket, 'removed', CONNECTIONS_REGISTRY)
        pass  # Nothing special required to do.


async def main():
    """Server 'orchestrator', setups config and start server"""
    port = 8765

    async with serve(connection_handler, "", port) as ws_server:
        log.debug(f"Starting websocket server on port {port}")
        log.debug(f"In mode: {CAST_MODE}")
        await ws_server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ki:
        log.debug("SIGTERM received from keyboard, terminating.")
        pass

# ========== INSTRUCTIONS =========
# Improve the Websocket Webserver from previous tasks, update it to...
# Broadcast a message received by one client to ALL currently known clients,
#   prefixing the message with 'B:' for clarity.

# ========== BRAINSTORM ==========
# To add the new behaviour while making as little breaking changes as possible
#   I will add a global variable "CAST_MODE" to choose whether to unicast
#   or broadcast and slightly update handler to have a "switch" upon it.
