from redis_functions import get_counter, increase_counter


async def check_anagrams(string_1, string_2):
    check_status = 'NO'
    if sorted(string_1.lower()) == sorted(string_2.lower()):
        await increase_counter()
        check_status = 'YES'
    counter = await get_counter()
    return {'anagram': check_status, 'counter': counter}
