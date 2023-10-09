## This is a Tabnine-generated program to play tic-tac-toe. It is a placeholder for the structure of a turn-based Pykémon battle.
import random
from mons import *

damage = random(0.8, 1) * (4 * (power * (attack / defense))/50)

charmander = Pykemon('Charmander', 4, 20, 20, 2, 4, 4, 6, Move()[''])

print("Bienvenido a Pykémon! ¿Te has preparado para el combate?")
print("Tu rival saca a Squirtle!")
print("¡Adelante, Charmander!")
while battle := True:
    print("----------------------------------------------------------------")
    print("¿Qué debería hacer Charmander?")
    print("----------------------------------------------------------------")
    cmd = input("------------LUCHAR--------------||--------------DATOS-----------")
    if cmd.casefold() == "luchar" :
        mv = input('''---------ARAÑAZO-----------||------------(vacío)---------\n
        ... ----------------------------------------------------------------
        ... ------------(vacío)-------------||------------(vacío)---------''')
        pass
    elif cmd.casefold() == "datos":
        pass
    else:
        throw ValueError("El comando ingresado no es válido.")

    

