import requests

from settings import TOKEN

TOKEN_YADISK = TOKEN
host = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def add_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.put(host, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.delete(host, headers=headers, params=params)
    return create_dir.status_code
