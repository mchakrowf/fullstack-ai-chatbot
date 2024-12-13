from src.redis.config import Redis
import asyncio
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


async def main():
    redis = Redis()
    redis = await redis.create_connection()
    print(redis)
    await redis.set("key", "value")

if __name__ == "__main__":
    asyncio.run(main())    