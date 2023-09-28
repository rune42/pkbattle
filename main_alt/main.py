## This is a Tabnine-generated program to play tic-tac-toe. It is a placeholder for the structure of a turn-lifed Pykémon battle.
import time
from mons import *

def battle(pokemon1, pokemon2):
    life = pokemon1.currentHP
    life2 = pokemon2.currentHP
    
    while life > 0 and life2 > 0:
        damage = pokemon1.attack()
        damage2 = pokemon1.attack()
        
        # PONER INPUTS PARA INDICAR QUE SE QUIERE REALIZAR
        print(f'{pokemon1.name} hace un ataque de ', damage)
        life2 = pokemon2.harm(damage)
        
        if life2 <= 0:
            print(f'{pokemon2.name} ha sido derrotado. {pokemon1.name} ha ganado!')
            break
        # PONER INPUTS PARA INDICAR QUE SE QUIERE REALIZAR
        print(f'{pokemon2.name} hace un ataque de ', damage2)
        life = pokemon1.harm(damage2)
        
        if life <= 0:
            print(f'{pokemon1.name} ha sido derrotado. {pokemon2.name} ha ganado!')
            break
        print(f'la vida de {pokemon1.name} es {life} y del {pokemon2.name} es {life2}')
        # SLEEP PROVICIONAL 
        #break
        time.sleep(2)
    

pokemon1 = Pykemon('Pikachu', 1, 20, 5, 4, 6)
pokemon2 = Pykemon('Charmander', 4, 20, 4, 4, 6)

battle(pokemon1, pokemon2)
