import requests

URL = 'https://api.pokemonbattle.ru'

TOKEN = '3a028b8762632a737170b226e50319b6'

HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_pokemons = {
    "name": "Малой",
    "photo_id": 101
}

response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_pokemons)

print(response.text)

pokemon_id = response.json()['id']

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Валентин",
    "photo_id": 102
}

rename = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_rename)

print(rename.text)

body_kill = {
    "pokemon_id": pokemon_id
}

kill_pokemon = requests.post(url = f'{URL}/v2/pokemons/knockout', headers = HEADER, json = body_kill)

print(kill_pokemon.text)