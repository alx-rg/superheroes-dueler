import random

class Weapon:
  def __init__(self, name, max_damage):
      self.name = name
      self.max_damage = max_damage
      
  def attack(self):
    random_value = random.randint((self.max_damage//2), self.max_damage)
    return random_value

if __name__ == "__main__":
  ability = Weapon('Debuggin fork', 20)
  print(ability.name)
  print(ability.attack())

