from .config import Redis

class Producer:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    #Takes the data and the Redis channel name.
    async def add_to_stream(self, data: dict, stream_channel):
        try:
            #Command for adding data to a stream channel is xadd and it has both high-level and low-level functions in aioredis.
            msg_id = await self.redis_client.xadd(name = stream_channel, id = "*", fields = data)
            print(f"Message id {msg_id} added to {stream_channel} stream")
            return msg_id
        except Exception as e:
            print(f"Error sending message to stream => {e}")