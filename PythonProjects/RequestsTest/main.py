import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '06236066cf81efed1c278e3079dc608b'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Pika",
    "photo_id": 2
},
body_change ={
    "pokemon_id": "42768",
    "name": "XXXppp",
    "photo_id": 6
},
body_pokeball={
    "pokemon_id": "42768"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print (response_pokeball.text)

