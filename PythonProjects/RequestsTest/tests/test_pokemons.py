import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '06236066cf81efed1c278e3079dc608b'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TREINER_ID = '4245'
NAME = 'Dash'

def test_status_code ():
    response = requests.get (url=f'{URL}/pokemons', params = {'treiner_id' : TREINER_ID} )
    assert response.status_code == 200

def test_part_of_response ():
    response_get = requests.get (url=f'{URL}/pokemons', params = {'treiner_id' : TREINER_ID, 'trainer_name' : NAME})