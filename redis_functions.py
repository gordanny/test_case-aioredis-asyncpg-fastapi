import aioredis


async def increase_counter(url='redis://localhost'):
    redis = await aioredis.create_redis(url)
    await redis.incrby('counter', 1)
    redis.close()
    await redis.wait_closed()


async def get_counter(url='redis://localhost'):
    redis = await aioredis.create_redis(url)
    counter = await redis.get('counter', encoding='UTF-8')
    redis.close()
    await redis.wait_closed()
    return counter
