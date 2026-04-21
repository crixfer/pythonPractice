import json
import requests
import sys

if len(sys.argv) != 2:
    print("You must write 'pokemon' after api.py")
    sys.exit()

response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=10 " + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

res = response.json()

for pokemon in res["results"]:
    print(pokemon["name"])