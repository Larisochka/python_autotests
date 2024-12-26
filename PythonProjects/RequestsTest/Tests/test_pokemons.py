import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '48819aa05ad5e38ff6b6e3ef40025d89'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
LEVEL = '3'
TRAINER_ID = "13862"

def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'level' : LEVEL})
    assert responce.status_code == 200


def test_part_of_responce():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == 'Ларик'

@pytest.mark.parametrize('key, value' , [('city' , 'Москва') , ('trainer_name' , 'Ларик'), ('id', '13862')])
def test_parametrize(key, value):
    responce_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_parametrize.json()["data"][0][key] == value