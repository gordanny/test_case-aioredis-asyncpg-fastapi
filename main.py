from fastapi import FastAPI

import redis_functions
import postgres_functions
import other_functions
import settings

app = FastAPI()


@app.post('/anagrams/{string_1}&{string_2}')
async def get_json(string_1: str, string_2: str):
    check = other_functions.check_anagrams(string_1, string_2)
    if check:
        await redis_functions.increase_counter(settings.redis['host'])
    counter = await redis_functions.get_counter(settings.redis['host'])
    return {'anagrams': check, 'counter': int(counter)}


@app.get('/postgres/fill', status_code=201)
async def fill_db():
    await postgres_functions.add_devices()
    await postgres_functions.add_endpoints()


@app.get('/postgres/devices')
async def get_devices_without_endpoints_json():
    selection = await postgres_functions.select_devices_without_endpoints()
    return selection
