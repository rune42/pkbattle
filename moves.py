
class Move:

  def __init__(self, name, maxPP, type, power):
    self.name = name
    self._maxPP = maxPP
    self.currentPP = maxPP
    self.type = type
    self._power = power
    self._critChance = 0.075
