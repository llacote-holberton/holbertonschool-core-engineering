#!/usr/bin/env python3

"""Echo server using the asyncio API."""

# ===== IMPORTS FOR FUNCTIONAL BEHAVIOUR =====
# Required to handle asynchronous tasks (imperative for websockets library)
import asyncio
# Using the provided "websockets-based server" from websockets library.
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed
# Used to generate unique ids easily.

# ===== SETTING UP LOGGING =====
import logging
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger('unicast_server')
logging.basicConfig(
    filename='unicast_server.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

# ===== SERVER FUNCTIONAL BEHAVIOUR =====
# Set to store active connections.
CONNECTIONS_REGISTRY = set()


async def connection_handler(websocket):
    """Creates a websocket handler to send validation on message received"""
    # This is the right level for try/except to explicit that...
    # "We try to discuss as long as connection is alive"
    debug_msg_tmpl = "ws %s %s, new registry state: %s"
    try:
        log.debug("New connection received!")
        CONNECTIONS_REGISTRY.add(websocket)
        # Suboptimal approach because Python will do the replacement even if
        #   the log technically shouldn't be display because wrong level'
        log.debug(debug_msg_tmpl, websocket, 'added', CONNECTIONS_REGISTRY)
        while (True):
            msg_received = await websocket.recv()
            # Putting try/except at this level useless since connection closed
            #   is destroyed so couldnd't "be repaired" on a later try.
            trimmed = msg_received.strip()
            if isinstance(trimmed, str) and len(trimmed) > 0:
                await websocket.send(f"OK: {trimmed}")
            else:
                await websocket.send("ERR:EMPTY")
    except ConnectionClosed as cc:
        CONNECTIONS_REGISTRY.discard(websocket)
        log.debug(debug_msg_tmpl, websocket, 'removed', CONNECTIONS_REGISTRY)
        pass  # Nothing special required to do.


# Serve is a corouting function, so needs "async" keyword,
#   thus "bubbling up" the need for async keyword up to main function.
async def main():
    """Server 'orchestrator', setups config and start server"""
    host = 'localhost'
    port = 8765
    ct = 2  # Option to restrict "finish current work" time (close_timeout)

    async with serve(connection_handler, "", port) as ws_server:
        log.debug(f"Starting websocket server on port {port}")
        await ws_server.serve_forever()


if __name__ == "__main__":
    # Remember: async function require being runned from
    #   library provided function.
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ki:
        log.debug("SIGTERM received from keyboard, terminating.")
        pass

# ========== INSTRUCTIONS =========
# Improve the Websocket Webserver from tasks 0 & 2, update it to...
# Be able to manage multiple clients while maintaining unicast communication
# Clients should be added/removed as required in a collection to keep track
#   of active connections.
# There should be no broadcast (yet).

# ========== BRAINSTORM ==========
# Concept of keeping track of multiples clients is "easy", we just need to
#   make a collection of any kind (List? Set? Dict? Will be refined later).
# But...
# 1) How to uniquely identify each client?
# 2) How can script know which message is associated with which client?
# 3) What to store in registry: just the "id"? The whole websocket?
# => Since any kind of "client id" would require either...
#    at minimum, a form of "contract" when we expect the client to include
#    some "id info" in request header or msg, and that is not in scope.
#    at maximum, a form of "id generation" from hashing request infos
#    like some websites cookies do, and that is *way* out of scope...
# => I'll just make a plain set (each connection should be a unique instance)
#    so it should automatically be "controlled" by the Set datatype.
#    Even though I don't fully understand why I guess it'

# === NOTES on using formatted strings in logger ===
# # Suboptimal approach because Python will do the replacement even if
# #   the log technically shouldn't be display because wrong level'
# log.debug(f"{websocket} added, registry state: {CONNECTIONS_REGISTRY}")
# Using the %* syntax makes Python ONLY replaces IF the message level matches
#   the configuration (ex if min level is ERROR, it would NOT process strings
#   for a DEBUG level message which is lower in priority.)

# === NOTES on adjusting server configuration to ensure a proper close ===
# I noticed that when throwing CTRL+C (SIGTERM) while at least one connection
#   was still active, the server never shut down.
# This was the consequences of two different mechanisms.
# 1) Whatever happens the server has a named parameter close_timeout
#    (default 10 sec) to allow any current transaction to finish.
# 2) In Websocket protocol includes a "still alive?" regular "ping"
#    (by default every 20 sec) to check that the connection is still valid
#    because it is the only way (other than trying an "active request") to
#    detect an interruption (connection closed anormally, network breakage)
# Reducing timeout would only affect "current transactions" but won't change
#   the server staying alive as long as a connection with a client is active.
# ONLY way would be to break conditionally to get out of the loop and thus
#   close the connection ourselves. For example
# try:
#     msg_received = await asyncio.wait_for(websocket.recv(), timeout=10.0)
# except asyncio.TimeoutError:
#     log.debug("Déconnexion forcée : Client inactif depuis 10 secondes.")
#     break
