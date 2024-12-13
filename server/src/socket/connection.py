from fastapi import WebSocket, WebSocketDisconnect
from typing import List


class ConnectionManager:
    def __init__(self):
        #List of active connections.
        self.active_connections: List[WebSocket] = []

    #Accept a WebSocket and add it to the list of active connections.
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    #Remove the Websocket from the list of active connections.
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    #Take in a message and the Websocket we want to send the message to and asynchronously send the message.    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)            