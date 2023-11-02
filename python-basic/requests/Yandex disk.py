import requests
from settings import TOKEN


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload_link(self, file_path):
        uri = "/v1/disk/resources/upload"
        url = self.host + uri
        filename = file_path.split('\\')[-1]
        params = {'path': f'\\{filename}', 'overwrite': 'true'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, file_path: str):
        upload_link = self.upload_link(file_path)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))
        if response.status_code == 201:
            return 'Загрузка прошла успешо'
        else:
            return f'Ошибка {response.status_code}'


if __name__ == '__main__':
    path_to_file = r'\Users\andre\OneDrive\Рабочий стол\bil.jpg'
    tokens = TOKEN
    uploader = YaUploader(tokens)
    print('Файл ' + path_to_file.split("\\")[-1] + ' загружается')
    result = uploader.upload(path_to_file)
    print(result)
