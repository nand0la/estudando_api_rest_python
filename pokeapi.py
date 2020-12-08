import requests

r = requests.get(f"https://pokeapi.co/api/v2/pokedex/2")
json_request = r.json()

for json_pokemons in json_request["pokemon_entries"]:
    print(json_pokemons["pokemon_species"]["name"])
    print(f"Saiba mais sobre o pokemon: {json_pokemons['pokemon_species']['url']}")
    print()
