import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

pokemon = input("Pokemon: ")
response = requests.get(base_url + pokemon)
poke_data = response.json()

name = poke_data["name"]
height = poke_data["height"]
moves = poke_data["moves"]

print(name)
print("height: " + str(height))
for move in moves:
    print(move)