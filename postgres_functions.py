import asyncpg
from random import choice

import other_functions
import settings


async def add_devices():
    query_params = {
        'query_type': 'insert',
        'table': 'devices',
        'columns': 'dev_id, dev_type',
        'data': "",
        'options': '',
    }
    conn = await asyncpg.connect(**settings.postgres)
    for _record in range(10):
        dev_id = other_functions.get_random_mac()
        dev_type = choice(settings.device_types)
        query_params['data'] = "'" + dev_id + "', '" + dev_type + "'"
        query = other_functions.get_query(query_params)
        await conn.execute(query)
    await conn.close()


async def add_endpoints():
    query_params = {
        'query_type': 'insert',
        'table': 'endpoints',
        'columns': 'device_id, comment',
    }
    selection = await select_ids()
    devices = []
    for record in selection:
        for id_value in record:
            devices.append(str(id_value))
    conn = await asyncpg.connect(**settings.postgres)
    for _record in range(5):
        device_id = choice(devices)
        devices.remove(device_id)
        ip_address = other_functions.get_random_ip_address()
        query_params['data'] = "'" + device_id + "', '" + ip_address + "'"
        query = other_functions.get_query(query_params)
        await conn.execute(query)
    await conn.close()


async def select_ids():
    query_params = {
        'query_type': 'select',
        'table': 'devices',
        'columns': 'id',
    }
    conn = await asyncpg.connect(**settings.postgres)
    query = other_functions.get_query(query_params)
    result = await conn.fetch(query)
    await conn.close()
    return result


async def select_devices_without_endpoints():
    query_params = {
        'query_type': 'select',
        'table': 'devices d, endpoints e',
        'columns': 'dev_type, COUNT(*)',
    }
    options = 'WHERE d.id = e.id GROUP BY dev_type'
    conn = await asyncpg.connect(**settings.postgres)
    query = other_functions.get_query(query_params, options)
    result = await conn.fetch(query)
    await conn.close()
    return result
