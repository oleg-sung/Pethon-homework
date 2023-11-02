import requests


def smartest_superhero(*args):
    superheroes_list = args
    superheroes_dict = {}
    response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    for superhero_info in response.json():
        for superhero in superheroes_list:
            if superhero_info['name'] == superhero:
                superheroes_dict[superhero_info['name']] = superhero_info["powerstats"]['intelligence']
    result = max(superheroes_dict, key=superheroes_dict.get)
    return f'Самый умный супергерой {result} c показателем интелектом: {superheroes_dict[result]}'


print(smartest_superhero("Hulk", "Captain America", "Thanos"))
