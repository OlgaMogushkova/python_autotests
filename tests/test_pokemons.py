import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3aed4b3c62b59c2bf640e66432b76cc5'
HEADER ={'Content-type' : 'application/json',
         'trainer_token' : TOKEN}
response_trainer_info = requests.get(url=f'{URL}/me', headers=HEADER)

TRAINER_ID = '38131'

def test_status_code_pokemons():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'bombucha'

@pytest.mark.parametrize('key, value', [('name', 'bombucha'), ('trainer_id', TRAINER_ID), ('id', '319594')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value

def test_status_code_trainers():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response_trainer():
    response_get = requests.get(url = f'{URL}/trainers/38131')
    assert response_get.json()['trainer_name'] == 'ABRICOT'
