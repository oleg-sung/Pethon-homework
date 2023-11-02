import pytest

from app import visit_filter, geo_logs, list_to_dictionary, unique_ids


class TestVisit:
    @pytest.mark.parametrize(
        'visit_list, country, expected', (
                (geo_logs, 'Россия', [
                    {'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}]),
                (geo_logs, 'Франция', [
                    {'visit5': ['Париж', 'Франция']}]),
                (geo_logs, 'Португалия', [
                    {'visit4': ['Лиссабон', 'Португалия']},
                    {'visit6': ['Лиссабон', 'Португалия']}

                ])
        )
    )
    def test_visit(self, visit_list, country, expected):
        result = visit_filter(visit_list, country)
        assert result == expected


class TestListDictionary:
    @pytest.mark.parametrize(
        "list_, expected", (
                (
                        ['2018-01-01', 'yandex', 'cpc', 100],
                        {'2018-01-01': {'yandex': {'cpc': 100}}}
                ),
                (
                        ['2018-01-01', 'yandex', 'cpc', 100, 43],
                        {'2018-01-01': {'yandex': {'cpc': {100: 43}}}}
                ),
                (
                        ['2023', 'google', 'cpc', 126],
                        {'2023': {'google': {'cpc': 126}}}
                )

        )
    )
    def test_list_to_dictionary(self, list_, expected):
        result = list_to_dictionary(list_)
        assert result == expected


class TestUniqueId:
    @pytest.mark.parametrize(
        "ids, expected", (({'user1': [213, 213, 213, 15, 213],
                            'user2': [54, 54, 119, 119, 119],
                            'user3': [213, 98, 98, 35]},
                           {213, 213, 213, 15, 54, 54, 119, 119, 119, 213, 98, 98, 35}
                           ),
                          )
    )
    def test_unique_id(self, ids, expected):
        result = unique_ids(ids)
        assert result == expected
