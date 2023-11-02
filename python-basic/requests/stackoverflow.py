import requests
import time


def questions(tag: str):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': round(time.time() - 172800),
              'todate': round(time.time()),
              'tagged': tag,
              'site': "stackoverflow",
              'pagesize': 100,
              'page': 1
              }
    questions_list = []
    while True:
        response = requests.get(url, params=params)
        params['page'] += 1
        for items_list in response.json()['items']:
            questions_list.append(items_list['link'])
        if not response.json()["has_more"]:
            return questions_list


print(len(questions('Python')))