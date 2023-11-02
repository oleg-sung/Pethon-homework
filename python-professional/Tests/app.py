geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def visit_filter(visit_list, country):
    duplicate_list = visit_list[:]
    for visits_dict in duplicate_list[:]:
        for visit in visits_dict.values():
            if country not in visit:
                duplicate_list.remove(visits_dict)
    return duplicate_list


def list_to_dictionary(list_):
    value = list_[-1]
    for key in list_[-2::-1]:
        value = {key: value}
    return value


def unique_ids(dikt_users):
    unique_id = set()
    for geo_id in dikt_users.values():
        geo_id = set(geo_id)
        unique_id |= geo_id
    return unique_id
