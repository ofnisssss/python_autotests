import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5cdcc9bfdb3d901916d68ad1d83e46b6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_newpokemon = {
    "name": "Лола",
    "photo_id": 7
}

body_namepokemon = {
    "pokemon_id": "136286",
    "name": "Лолита",
    "photo_id": 7
}

body_add_pokeball = {
    "pokemon_id": "136286"
}

"""response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_newpokemon)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_namepokemon)
print(response.text)"""

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response.text)