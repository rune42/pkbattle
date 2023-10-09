## This is a Tabnine-generated program to play tic-tac-toe. It is a placeholder for the structure of a turn-based Pykémon battle.
import random

class Pykemon:
    def __init__(self, name, dexNum, currentHP, baseHP, baseAtk, baseDef, baseSpd, moveSet):
        self.dexNum = dexNum
        self.name = name
        self.currentHP = currentHP
        self.baseHP = baseHP
        self.baseAtk = baseAtk
        self.baseDef = baseDef
        self.baseSpd = baseSpd
        self.moveSet = moveSet

    def harm(self, damage):
        self.currentHP -= damage

    def heal(self, healing):
        if self.currentHP + healing <= self.maxHP:
            self.currentHP += healing
        else:
            self.currentHP = self.maxHP

class Move:
    def __init__(self, name, maxPP, type, power):
        self.name = name
        self._maxPP = maxPP
        self.currentPP = maxPP
        self.type = type
        self._power = power
        self._critChance = 0.075

    def attack(self, attacker, defender):
        if isinstance(attacker, Pykemon) and isinstance(defender, Pykemon):
            if self.currentPP > 0:
                damage = (random.uniform(0.8, 1) * (4 * self.power * (attacker.baseAtk / defender.baseDef)) / 50)
                self.currentPP -= 1
                return damage
            else:
                print("¡No quedan PP para usar este ataque!")
                return None


if __name__ == '__main__':

    charmander = Pykemon('Charmander', 4, 20, 20, 2, 4, 4, 6, Move()[''])

    print("Bienvenido a Pykémon! ¿Te has preparado para el combate?")
    print("Tu rival saca a MISSINGNO.!")
    print("¡Adelante, MISSINGNO.!")
    while all(pykemon.currentHP > 0 for pykemon in self.pykemons):
            for i in range(len(self.pykemons)):
                attacker = self.pykemons[i]
                defender = self.pykemons[(i+1)%len(self.pykemons)]

                damage = attacker.attack()
                print(f'{attacker.name} hace un ataque de {damage}')
                defender.harm(damage)

                if defender.currentHP <= 0:
                    print(f'{defender.name} ha sido derrotado. {attacker.name} ha ganado!')
                    return

                print(f'La vida de {attacker.name} es {attacker.currentHP} y del {defender.name} es {defender.currentHP}')
                time.sleep(2)
    # 
    # while battle := True:
    #     print("----------------------------------------------------------------")
    #     print("¿Qué debería hacer Charmander?")
    #     print("----------------------------------------------------------------")
    #     cmd = input("------------LUCHAR--------------||--------------DATOS-----------")
    #     if cmd.casefold() == "luchar" :
    #         mv = input('''---------ARAÑAZO-----------||------------(vacío)---------\n
    #         ... ----------------------------------------------------------------
    #         ... ------------(vacío)-------------||------------(vacío)---------''')
    #         pass
    #     elif cmd.casefold() == "datos":
    #         pass
    #     else:
    #         throw ValueError("El comando ingresado no es válido.")

