from fastapi import FastAPI

from check_anagrams import check_anagrams
from redis_functions import increase_counter, get_counter

app = FastAPI()
redis_url = 'redis://localhost'


@app.post('/anagram/{string_1}&{string_2}')
async def get_json(string_1: str, string_2: str):
    """Increases the counter value in Redis if the received strings are anagrams.
    Returns json with the counter value from the Redis and
    the result of checking whether the compared strings are anagrams.
    """
    check = check_anagrams(string_1, string_2)
    if check:
        await increase_counter(redis_url)
    counter = await get_counter(redis_url)
    return {'anagram': check, 'counter': int(counter)}
