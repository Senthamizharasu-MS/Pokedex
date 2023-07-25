import requests
import json
import os
import time
from colorama import Fore
from colorama import init
init(autoreset=True)

def getPokémonName():
    time.sleep(1)
    clear()
    name = input(Fore.GREEN + "Enter a Pokémon name or id: ")
    return name

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getPokemonData(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    response = requests.get(url)
    if response.text == "Not Found":
        print(Fore.RED + "Pokémon not found!")
        # sys.exit()
        getPokémonName()
    data = json.loads(response.text)
    return data

def getPokemonTypes(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    response = requests.get(url)
    data = json.loads(response.text)
    return data.get("types")

def getPokemonImage(pokemon):
    url = "https://img.pokemondb.net/artwork/" + pokemon + ".jpg"
    return url


if __name__ == "__main__":

    print(Fore.GREEN + "Welcome to the Pokédex!")
    time.sleep(3)
    clear()

    name = getPokémonName()
    pokemon = getPokemonData(name)

    print(Fore.GREEN + "Pokémon data:")
    print(Fore.GREEN + "ID: " + str(pokemon.get("id")))
    print(Fore.GREEN + "Name: " + pokemon.get("name"))

    pokemonTypes = getPokemonTypes(name)
    for i in range(0, len(pokemonTypes)):
        pokemonTypes[i] = pokemonTypes[i].get("type").get("name")
        print(Fore.GREEN + "Type " + str(i + 1) + ": " + pokemonTypes[i])

    image = getPokemonImage(name)
    print(Fore.GREEN + "Image: " + image)
