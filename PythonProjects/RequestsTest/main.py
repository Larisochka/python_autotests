import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '48819aa05ad5e38ff6b6e3ef40025d89'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Bobo",
    "photo_id": 233
}

body_add = {
    "pokemon_id": '171597'
}

body_change_name = {
    "pokemon_id": '171597',
    "name": "New Name"
}


responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)

## Создать покемона

responce_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(responce_add.text)

## Поймать в покебол

responce_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(responce_change_name.text)

## Изменить имя

