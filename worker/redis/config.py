import os
from dotenv import load_dotenv
import aioredis

load_dotenv()

#Create a Redis object
class Redis():
    def __init__(self):
        """initialize connection """
        #Initialize the required parameters from the environment variables.
        self.REDIS_URL = os.environ['REDIS_URL']
        self.REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
        self.REDIS_USER = os.environ['REDIS_USER']
        self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"
    #Create a Redis connection and return the connection pool obtained from the aioredis method from_url.
    async def create_connection(self):
        self.connection = aioredis.from_url(
            self.connection_url, db = 0
        )
        return self.connection

