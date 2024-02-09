import sys
import asyncio
from websockets.sync.client import connect

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 8765

def hello():
    with connect("ws://web-socket-server:8765") as websocket:
        websocket.send("Hello World!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()