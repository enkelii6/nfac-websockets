from fastapi.responses import HTMLResponse


async def home():
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat</title>
        </head>
        <body>
            <h1>WebSocket Chat</h1>

            <form id="nameForm" onsubmit="connectWebSocket(event)">
                <label for="nameInput">Name:</label>
                <input type="text" id="nameInput" autocomplete="off" required/>
                <button type="submit">Join</button>
            </form>

            <form id="chatForm" onsubmit="sendMessage(event)" style="display:none;">
                <input type="text" id="messageText" autocomplete="off" />
                <button type="submit">Send</button>
            </form>

            <ul id='messages'></ul>

            <script>
                let ws = null;

                function connectWebSocket(event) {
                    event.preventDefault();

                    const name = document.getElementById("nameInput").value.trim();
                    if (!name) return;

                    ws = new WebSocket("ws://localhost:8000/chat?name=" + encodeURIComponent(name));

                    ws.onopen = () => {
                        document.getElementById("nameForm").style.display = "none";
                        document.getElementById("chatForm").style.display = "block";
                        document.getElementById("messageText").focus();
                    };

                    ws.onmessage = function(event) {
                        var messages = document.getElementById('messages');
                        var message = document.createElement('li');
                        var content = document.createTextNode(event.data);
                        message.appendChild(content);
                        messages.appendChild(message);
                    };
                }

                function sendMessage(event) {
                    event.preventDefault();

                    const input = document.getElementById("messageText");
                    const text = input.value.trim();
                    if (text && ws) {
                        ws.send(text);
                        input.value = '';
                    }
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(html)
