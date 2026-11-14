import random

import requests

pokemon_list = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee"]


def get_pokemon(name):
    normalized_name = name.lower().strip()
    url = f"https://pokeapi.co/api/v2/pokemon/{normalized_name}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print("Pokemon not found!")
            return None

        response.raise_for_status()
        data = response.json()

        pokemon_name = data["name"]
        height = data["height"]
        weight = data["weight"]

        return pokemon_name, height, weight

    except requests.exceptions.RequestException:
        print("Connection error. Please check your internet.")
        return None

    except (ValueError, KeyError):
        print("There was a problem getting the Pokemon data.")
        return None


def play_game():
    print("==============================")
    print("      WHO'S THAT POKEMON?")
    print("==============================")

    chosen = random.choice(pokemon_list)
    pokemon = get_pokemon(chosen)

    if pokemon is None:
        return

    name, height, weight = pokemon

    print("\nGuess the Pokemon using its height and weight!")
    print("Height:", height, "dm")
    print("Weight:", weight, "hg")

    for attempt in range(1, 4):
        guess = input("\nEnter your guess: ").lower().strip()

        if guess == "":
            print("Please enter a Pokemon name.")
            continue

        if guess == name.lower():
            print("Correct! You win!")
            return

        print("Wrong answer!")
        print("Attempts left:", 3 - attempt)

    print("\nGame over!")
    print("The correct Pokemon was:", name)


if __name__ == "__main__":
    play_game()