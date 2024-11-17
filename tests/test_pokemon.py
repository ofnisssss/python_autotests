import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5cdcc9bfdb3d901916d68ad1d83e46b6'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7192'


def test_status_code_trainers():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200
