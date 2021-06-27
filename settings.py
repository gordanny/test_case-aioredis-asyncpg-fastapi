from os import environ

postgres = {
    'host': environ.get('db_host'),
    'user': environ.get('db_user'),
    'password': environ.get('db_pass'),
    'database': environ.get('db_name'),
}

redis = {
    'host': environ.get('redis_host'),
}

device_types = (
    'emeter',
    'zigbee',
    'lora',
    'gsm'
)
