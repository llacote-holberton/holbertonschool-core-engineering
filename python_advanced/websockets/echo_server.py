#!/usr/bin/env python3

"""Echo server using the asyncio API."""

# Required to handle asynchronous tasks (imperative for websockets library)
import asyncio
# Using the provided "websockets-based server" from websockets library.
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Creates a websocket handler to echo message"""
    async for msg_received in websocket:
        await websocket.send(msg_received)


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
    asyncio.run(main())

# ========== INSTRUCTIONS =========
# Implement a WebSocket server with websockets and async.io libraries that:
# * Listens on localhost at port 8765 until server is shut down
# * (not after single message)
# * Accepts multiple client connections
# * Receives text messages from a client and "echoes them" (send back same)
#     as soon as they are received (no batching or delays)
# Only text messages need to be supported
# The server must start when calling script as argument of python3 interpreter.

# ========== BRAINSTORM ==========
# === Notes about the async with serve(...) as myserver syntax
# with keyword ensures the server closes properly, once
#   all instructions inside the block are executed.
# Technically the with ... as x syntax is just calling
#   the dunders __enter__ / __exit__ (or aenter/aexit for async variants)
#   implemented by the object / expression written in ...
# Serve is a function setting up a websocket server with a reference to
#   a "handler function". Upon receiving a connection the server will
#   automatically call the handler while creating on the fly the required
#   "websocket" parameter object.
# Second argument can be used to restrict the network interfaces on which
#   to listen, "" = "listen everywhere". Third is machine port to use.
# async with serve(connection_handler, "", port) as ws_server:
#     # This specific instruction will prevent the server from
#     #   closing "normally". Will need either explicit call to server.close
#     #   or KeyboardInterrupt.
#     await ws_server.serve_forever()
# === Notes about the custom handler ===
# print("Websocket attributes", dir(websocket))
# @note: this is the way to handle a single request per connection
# msg_received = await websocket.recv()
# await websocket.send(msg_received)
# The connection will be closed automatically afterwards so IF the client
#   wants another "transaction" it would need to recreate a new connection.
# Note: this works because Websocket object implements __aiter__ dunder
#   to create an asynchronous generator which "yields" items.
# async for msg_received in websocket:
#     # @warning: we directly receives the message stream from how
#     #   the generator was designed.
#     # Keeping this line would override message n with the n+1.
#     # msg_received = await websocket.recv()
#     await websocket.send(msg_received)
