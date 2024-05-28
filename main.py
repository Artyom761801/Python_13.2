import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '899c79a0e001099b58c0b8aa1c23028a'
HEADER = {'Comtent-Type':'application/json', 'trainer_token':TOKEN}
#Создание покемона
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

#Смена имени покемона
body_pokemons2 = {
    "pokemon_id": pokemon_id,
    "name": "Бульбазубр",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons2)
print(response_name.text)

#Поймать покемона в покебол
body_pokemons3 = {
    "pokemon_id": pokemon_id
}
response_pok = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemons3)
print(response_pok.text)
