#!/usr/bin/env python3
"""Simple websocket client."""

# Required to handle asynchronous tasks (imperative for websockets library)
import asyncio
# Using the provided "websockets-based connect" from websockets library.
from websockets.asyncio.client import connect


async def connect_and_send(ws_server_url: str, msg_to_send: str):
    """Tries to send a given message to target websocket uri"""
    try:
        async with connect(ws_server_url) as websocket:
            await websocket.send(msg_to_send)
            received_echo = await websocket.recv()
            return received_echo
    except OSError as e:
        pass  # Connection couldn't be established.
    except ConnectionClosed as e:
        pass  # Connection was closed while we were discussing.


# Connect is a corouting function => needs async main
async def main():
    """Server 'orchestrator', setups config and start server"""

    protocol = 'ws://'
    host = 'localhost'
    port = 8765
    ws_server_url = protocol + host + ':' + str(port)

    msg_to_send = "Hello WebSocket"

    echo_received = await connect_and_send(ws_server_url, msg_to_send)
    print(echo_received)

if __name__ == "__main__":
    # Remember: async function require being runned from
    #   library provided function.
    asyncio.run(main())

# ========== INSTRUCTIONS =========
# Implement a WebSocket client which will...
# * Send exactly this message "Hello WebSocket" to a server ws://localhost:8765
# * Wait for the server's response and print it
#   (sent message and received response should be exactly the same string).
# * Closes the connection afterwards.

# ========== BRAINSTORM ==========
