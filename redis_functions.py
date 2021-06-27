import aioredis
import settings


async def increase_counter(host: str = settings.redis['host'], value: int = 1):
    redis = await aioredis.create_redis(host)
    await redis.incrby('counter', value)
    redis.close()
    await redis.wait_closed()


async def get_counter(host: str = settings.redis['host']):
    redis = await aioredis.create_redis(host)
    counter = await redis.get('counter', encoding='UTF-8')
    redis.close()
    await redis.wait_closed()
    return counter
