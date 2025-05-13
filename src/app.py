import uvicorn
from fastapi import FastAPI, Response, status

from src.handlers import home
from src.websockets import chat

app = FastAPI()


app.add_api_websocket_route('/chat', chat)
app.add_api_route('/', home)


@app.get('/health')
async def health():
    return Response(status_code=status.HTTP_200_OK)


if __name__ == '__main__':
    uvicorn.run('src.app:app', host='0.0.0.0', port=8000, reload=True)
