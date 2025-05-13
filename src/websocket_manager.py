from fastapi import WebSocket


class WebsocketManager:
    def __init__(self):
        self.clients = []

    async def connect(self, websocket: WebSocket, name: str):
        self.clients.append({'ws': websocket, 'name': name})

    async def disconnect(self, websocket: WebSocket):
        for client in self.clients:
            if websocket == client['ws']:
                self.clients.remove(client)

    async def broadcast(self, message: str, name: str):
        for client in self.clients:
            await client['ws'].send_text(f'{name}: {message}')


websocket_manager = WebsocketManager()
