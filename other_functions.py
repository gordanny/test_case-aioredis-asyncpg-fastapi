from random import randrange


def check_anagrams(string_1: str, string_2: str):
    check = sorted(string_1.lower()) == sorted(string_2.lower())
    return check


def get_random_mac():
    octets = []
    for _octet in range(6):
        octet = hex(randrange(256)).replace('0x', '').zfill(2)
        octets.append(octet)
    mac = ':'.join(octets)
    return mac


def get_random_ip_address():
    octets = []
    for _octet in range(4):
        octet = str(randrange(256))
        octets.append(octet)
    ip_address = '.'.join(octets)
    return ip_address


def get_query(parameters: dict, options: str = ''):
    if parameters['query_type'] == 'select':
        query = f"""SELECT {parameters['columns']} FROM {parameters['table']} 
    """ + options
    elif parameters['query_type'] == 'insert':
        query = f"""INSERT INTO {parameters['table']} ({parameters['columns']})
        VALUES ({parameters['data']}) 
    """ + options
    else:
        query = ''
    return query
