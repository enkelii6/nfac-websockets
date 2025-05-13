from fastapi import WebSocket

from src.websocket_manager import websocket_manager


async def chat(websocket: WebSocket, name: str):
    await websocket.accept()
    await websocket_manager.connect(websocket, name)

    while True:
        msg = await websocket.receive_text()
        await websocket_manager.broadcast(msg, name)
