import requests
import pytest

URL = 'https://api.pokemonbattle.ru'

TOKEN = '3a028b8762632a737170b226e50319b6'

HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

TRAINER_ID = '4911'

def test_status():
    respons_code = requests.get(url= f'{URL}/v2/trainers')
    assert respons_code.status_code == 200

def test_trainername():
    respons_name = requests.get(url= f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID})
    assert respons_name.json()['data'][0]['trainer_name'] == "Компот"
