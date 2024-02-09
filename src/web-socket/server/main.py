import sys
import asyncio
from websockets.server import serve

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 8765

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, '0.0.0.0', PORT):
        await asyncio.Future()

asyncio.run(main())