#!/usr/bin/env python3

"""Echo server using the asyncio API."""

# Required to handle asynchronous tasks (imperative for websockets library)
import asyncio
# Using the provided "websockets-based server" from websockets library.
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Creates a websocket handler to send validation on message received"""
    # This is the right level for try/except to explicit that...
    # "We try to discuss as long as connection is alive"
    try:
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
        pass  # Nothing special required to do.


# Serve is a corouting function, so needs "async" keyword,
#   thus "bubbling up" the need for async keyword up to main function.
async def main():
    """Server 'orchestrator', setups config and start server"""
    host = 'localhost'
    port = 8765

    async with serve(connection_handler, "", port) as ws_server:
        await ws_server.serve_forever()


if __name__ == "__main__":
    # Remember: async function require being runned from
    #   library provided function.
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ki:
        pass

# ========== INSTRUCTIONS =========
# Improve the Websocket Webserver from task 0, update it to...
# * Receive text messages from connected clients
# * Validate each message before responding, and responding adequately.
# Is considered invalid "empty strings" post pre/post trimming.

# ========== BRAINSTORM ==========

# === Notes about using the custom handler with try/except ===
# Doing this
# try:
#     async for msg_received in websocket:
#     ...
# except ConnectionClosed as e:
#     ...
# Will NOT work because...
# Internally the "for xxx" makes regular calls to websocket.recv()
# When/IF the connection is closed, recv() raises the ConnectionClosed error
# BUT it is silently catched by the iterator itself and "transformed" into
#   a "normal end of iteration" aka StopAsyncIteration.
# Making this...
# async for msg_received in websocket:
#     try:
#         ...
#     except:
#         ...
# Would only catch the exception if it happens during the send.
# => ONLY WAY to properly catch the exception whether in receiption or sending
#    is to NOT use the built-in iterator with for xxx in websocket syntax
#    INSTEAD to define an explicitely infinite loop (while True) with
#    EXPLICIT break cases.
#    Benefit of that though is that we could define all related catchs
#      in the same place (for example defining custom Exceptions for empty msg)

# === Notes on trimming received message ===
# Good practice to strim "empty spaces" around string to...
# 1. Facilitate comparison
# 2. Avoid differences from messages sent from different clients/OS
#    which may or not add new line.
# Also for this task it is explicitely required.

# === Notes on handling Keyboard Interrupt SIGTERM signal ===
# # Good (or required xd) practice to properly handle explicit extinctions
# try:
#     async with serve(connection_handler, "", port) as ws_server:
#         await ws_server.serve_forever()
# except KeyboardInterrupt as ki:
#     pass
# EXCEPT IT WOULDN'T WORK BECAUSE
#   the KeyboardInterrupt would be received and handled by asyncio.run()
#   which would first send an asyncio.CancelledError to main() to stop it
#   then propagate the KeyboardInterrupt exception.
# Hence why it MUST be catched "around the asyncio.run" level.
