import json

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

from logger_v2 import logger


def get_headers():
    return Headers(browser='yandex', os='win').generate()


@logger(path='vacancies.log')
def fresh_vacancies_hh(host):
    params = {
        'text': 'Python',
        'area': [1, 2],
        'per_page': 100,
        'page': 0
    }
    main_page = requests.get(host, headers=get_headers(), params=params).text
    bs = BeautifulSoup(main_page, features='lxml')
    vacancies_list = bs.find(class_="vacancy-serp-content")
    vacancies_tag = vacancies_list.find_all(class_='serp-item')
    job_list = []
    for vacancy_tag in vacancies_tag:
        title = vacancy_tag.find('h3').find('span').text
        links = vacancy_tag.find('a')['href']
        salary = vacancy_tag.find(class_="vacancy-serp-item-body__main-info").find_all('span')[2].text
        company = vacancy_tag.find(class_="bloko-text").find('a').text
        city = vacancy_tag.find(class_="vacancy-serp-item__info").find_all(class_="bloko-text")[-1].text
        description = requests.get(links, headers=get_headers()).text
        bs1 = BeautifulSoup(description, features='lxml')
        text = bs1.find(class_='g-user-content').text
        if 'Django' in text or 'Flask' in text:
            job_list.append({
                'title': title,
                'links': links,
                'salary': salary.replace(u"\u202F", " "),
                'company': company.replace(u"\u202F", " "),
                'city': city.replace(u"\u202F", " ")
            })
    with open("data_file.json", 'w', encoding='UTF-8') as f:
        json.dump(job_list, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    HOST = 'https://spb.hh.ru/search/vacancy'
    fresh_vacancies_hh(HOST)
