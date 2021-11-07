import random

class Team:
  def __init__(self, name):
      self.name = name
      self.heroes = list()
      
  def add_hero(self, hero):
    self.heroes.append(hero)

  def remove_hero(self, name):    
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        return True
      return False

  def view_all_heroes(self):
      for hero in self.heroes:
        print(f'{hero.name}')

  def stats(self):
    for hero in self.heroes:
      kd = hero.kills / (hero.deaths or 1)
      print(f'{hero.name} Kill/Deaths: {kd}')

  def revive_heroes(self, health=100):
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  def attack(self, other_team):
    living_heroes = []
    living_opponents = []

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents) > 0:
      self_hero = random.choice(living_heroes)
      other_hero = random.choice(living_opponents)
      if self_hero.fight(other_hero) == 'win':
        living_heroes.remove(self_hero)
      else:
        living_opponents.remove(other_hero)
