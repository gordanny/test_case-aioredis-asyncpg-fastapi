from fastapi import FastAPI

from check_anagrams import check_anagrams

app = FastAPI()

redis_url = 'redis://localhost'


@app.post('/anagram/{string_1}&{string_2}')
async def get_json(string_1: str, string_2: str):
    json = await check_anagrams(string_1, string_2)
    return json
