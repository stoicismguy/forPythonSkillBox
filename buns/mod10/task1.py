import requests
import json

starship = requests.get(url="https://swapi.dev/api/starships/?search=Millennium Falcon").json()['results'][0]

info = dict()
info['ship_name'] = starship['name']
info['max_atmosphering_speed'] = starship['max_atmosphering_speed']
info['starship_class'] = starship['starship_class']

info['pilots'] = [{'name': p['name'],
                   'height': p['height'],
                   'mass': p['mass'],
                   'homeworld_url': p['homeworld'],
                   'homeworld': requests.get(url=p['homeworld']).json()["name"]} for p in [requests.get(url=url).json() for url in starship['pilots']]]
print(info)

with open('D:/output.json', 'w+') as file:
    json.dump(info, file)
