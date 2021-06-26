import aioredis


async def increase_counter(url='redis://localhost', value=1):
    """Increasing the counter value in Redis dictionary."""
    redis = await aioredis.create_redis(url)
    await redis.incrby('counter', value)
    redis.close()
    await redis.wait_closed()


async def get_counter(url='redis://localhost'):
    '''Getting the counter value from the Redis dictionary.'''
    redis = await aioredis.create_redis(url)
    counter = await redis.get('counter', encoding='UTF-8')
    redis.close()
    await redis.wait_closed()
    return counter
