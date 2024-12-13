#Import FastAPIand initilize it as api
from fastapi import FastAPI, Request
import uvicorn
import os
#Import load_dotenv from the python-dotenv library
from dotenv import load_dotenv
#Connect the chat route to our main API
from src.routes.chat import chat

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


load_dotenv()

api = FastAPI()
api.include_router(chat)

#Create a simple test route to test the API. The test route will return a simple JSON response that tells us the API is online.
@api.get("/test")
async def root():
    return {"msg": "API is Online"}

#Set up the development server by using uvicorn.run and providing the required arguments.
if __name__ == "__main__":
    if os.environ.get('APP_ENV') == "development":
        #The API will run on port 3500
        uvicorn.run("main:api", host="0.0.0.0", port=3500,
                    workers=4, reload=True)
    else:
      pass