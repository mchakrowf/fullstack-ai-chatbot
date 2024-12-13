import os
from fastapi import APIRouter, FastAPI, WebSocket, Request, BackgroundTasks, HTTPException, WebSocketDisconnect
import uuid
from src.socket.connection import ConnectionManager
from src.socket.utils import get_token
from src.redis.config import Redis
from src.redis.producer import Producer
from fastapi import Depends



chat = APIRouter()
manager = ConnectionManager()
redis = Redis()
producer = Producer(redis)
#We created three endpoints:





#Will issue the user a session token for access to the chat session.
# @route   POST /token
# @desc    Route to generate chat token
# @access  Public
@chat.post("/token")
async def token_generator(name: str, request: Request):
    
    #We do a quick check to ensure that the name field is not empty
    if name == "":
        raise HTTPException(status_code=400, detail={"loc": "name", "msg": "Enter a valid name"})
    
    #To generate a user token we will use uuid4 to create dynamic routes for our chat endpoint.
    token = str(uuid.uuid4())

    data = {"name": name, "token": token}

    return data





#Will get the session history for the user if the connection is lost, as long as the token is still active and not expired.
# @route   POST /refresh_token
# @desc    Route to refresh token
# @access  Public
@chat.post("/refresh_token")
async def refresh_token(request: Request):
    return None






#Will open a WebSocket to send messages between the client and server.
# @route   Websocket /chat
# @desc    Socket for chatbot
# @access  Public
@chat.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_token)):
    #We add the new websocket to the connection manager
    await manager.connect(websocket)
    try:
        #The socket stays open
        while True:
            #Receive any messages sent by the client 
            data = await websocket.receive_text()
            print(data)
            stream_data = {}
            stream_data[token] = data
            await producer.add_to_stream(stream_data, "message_channel")
            await manager.send_personal_message(f"Response: Simulating response from the GPT service", websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)