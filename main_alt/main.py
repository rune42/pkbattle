## This is a Tabnine-generated program to play tic-tac-toe. It is a placeholder for the structure of a turn-based Pykémon battle.
import random, time
from mons import *

def battle(pokemon1, pokemon2):
    attack1 = pokemon1.currentHP
    attack2 = pokemon2.currentHP
    while attack1 > 0 and attack2 > 0:
        print(f'{pokemon1.name} hace un ataque de ', pokemon1.attack())
        attack1 -= pokemon1.attack()
        print(f'{pokemon2.name} hace un ataque de ', pokemon2.attack())
        attack2 -= pokemon2.attack()
        print(f'la vida de {pokemon1.name} es {attack1} y del {pokemon2.name} es {attack2}')
        time.sleep(2)

pokemon1 = Pykemon('Pikachu', 1, 20, 20, 5, 4, 6)
pokemon2 = Pykemon('Charmander', 4, 20, 20, 4, 4, 6)

battle(pokemon1, pokemon2)
