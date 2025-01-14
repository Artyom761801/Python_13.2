import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '899c79a0e001099b58c0b8aa1c23028a'
HEADER = {'Comtent-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2652'

def test_ststus_code():
    response = requests.get(url = f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Артём93'