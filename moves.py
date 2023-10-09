
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
