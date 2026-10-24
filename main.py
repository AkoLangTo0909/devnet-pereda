import random
import requests
poke = requests.get("https://pokeapi.co/pikachu,squirtle")

pick = {"Pikachu" ,"Bulbasaur" ,"Squirtle","Charmander","Snorlax"}

pokemon = print(input("Who's that Pokemon? :"))
random_poke = random.choice(poke)
print("Randomly selected pokemon:",random_poke)
print 

def my_pokemon():
    guess

