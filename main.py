import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3aed4b3c62b59c2bf640e66432b76cc5'
HEADER ={'Content-type' : 'application/json',
         'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "starykh.ola-la@yandex.ru",
    "password": "Iloveqa12345"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "bombucha",
    "photo_id": 15
}

body_knockout = {
    "pokemon_id": "319592"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json = body_registration)
print(response.text)''' #Регистрация

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json = body_confirmation) 
print(response_confirmation.text)''' #Подтверждение почты

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = body_create) 
print(response_create.text)

pokemon_id = response_create.json()["id"]
print(pokemon_id)''' #Создание покемона

'''response_knockout = requests.post(url=f'{URL}/pokemons/knockout', headers=HEADER, json=body_knockout)
print(response_knockout.text)''' #Отправить в нокаут своего покемона

response_trainer_info = requests.get(url=f'{URL}/me', headers=HEADER)
print(response_trainer_info.text) #Информация о тренере

TRAINER_ID = response_trainer_info.json()["data"] [0] ["id"]
print(TRAINER_ID) #Создание переменной ID тренера

POKEMON_ID = response_trainer_info.json()["data"] [0] ["pokemons"] [0]
print(POKEMON_ID)

body_changing_name = {
    "pokemon_id": POKEMON_ID,
    "name": "Abricos",
    "photo_id": 55
}

body_catch = {
    "pokemon_id": POKEMON_ID
}
response_changing_name = requests.put(url=f'{URL}/pokemons', headers=HEADER, json = body_changing_name)
print(response_changing_name.text) #сменить имя первому покемону из списка

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print(response_catch.text)