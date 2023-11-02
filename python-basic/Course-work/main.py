import requests
import json
from settings import TOKEN_VK
from collections import Counter
from datetime import datetime
from progressBar import ProcessBar


class VK:

    def __init__(self, access_token_, user_id_, version='5.131'):
        self.token = access_token_
        self.id = user_id_
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def avatar_info(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'album_id': 'profile',
                  'extended': 1,
                  'owner_id': f'{self.id}',
                  'photo_sizes': 1
                  }
        response = requests.get(url, params={**self.params, **params})
        return response.json()['response']

    def avatar_max(self):
        photo_list = []
        for photo in self.avatar_info()['items']:
            photo_sort = sorted(photo['sizes'], key=lambda x: x['type'], reverse=True)
            photo_list.append({
                'url': photo_sort[0]['url'],
                'likes': photo['likes']['count'],
                'date': photo['date'],
                'size': photo_sort[0]['type'],
                'pixels': photo_sort[0]['width'] * photo_sort[0]['height']
            })
        return sorted(photo_list, key=lambda x: x['pixels'], reverse=True)


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def add_folder(self, folder_name='photo vk'):
        uri = "/v1/disk/resources"
        url = self.host + uri
        params = {'path': folder_name}
        requests.put(url, headers=self.get_headers(), params=params)
        return folder_name

    def upload_photo(self, number_photos=5):
        bar = ProcessBar(len(vk.avatar_max()[:number_photos]))
        self.add_folder()
        uri = '/v1/disk/resources/upload'
        url = self.host + uri
        number_likes = Counter([i['likes'] for i in vk.avatar_max()[:number_photos]])
        log_file = []
        for photo in vk.avatar_max()[:number_photos]:
            params = {
                'path': f'/{self.add_folder()}/{photo["likes"]}.jpg',
                'url': photo['url']
            }
            if number_likes[photo['likes']] > 1:
                date = str(datetime.utcfromtimestamp(photo["date"]).strftime("%Y-%m-%d"))
                params = {
                    'path': f'/{self.add_folder()}/{photo["likes"]} | {date}.jpg',
                    'url': photo['url']
                }
            response = requests.post(url, headers=self.get_headers(), params=params)
            if response.status_code == 202:
                log_file.append({
                    'file_name': f'{photo["likes"]}.jpg',
                    'size': photo['size']
                })
                bar.update(f"Загрузка файла {photo['likes']}.jpg завершена !")
            print()
        with open("log file.json", 'w', encoding='UTF-8') as f:
            json.dump(log_file, f, indent=2)


if __name__ == "__main__":
    access_token = TOKEN_VK
    user_id = str(input('Введите id пользователя: '))
    vk = VK(access_token, user_id)
    token_ya = str(input('Введите токен "Яндекс Диска": '))
    ya = YaUploader(token_ya)
    ya.upload_photo()
