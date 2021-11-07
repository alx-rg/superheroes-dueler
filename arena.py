from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from validate_input import validate_input


class Arena:
  def __init__(self):
      self.team_one: None
      self.team_two: None

  def create_ability(self):
    name = validate_input('What is the ability name?', str)
    max_damage = validate_input('What is the max damage of the ability? ', int)
    return Ability(name, max_damage)

  def create_weapon(self):
    name = validate_input('What is the WEapON name?', str)
    max_damage = validate_input('What is the max damage of the WeApOn? ', int)
    return Weapon(name, max_damage)

  def create_armor(self):
    name = validate_input('What is the Armor name?', str)
    max_damage = validate_input('What is the max defence of the arm0r? ', int)
    return Armor(name, max_damage)

  def create_hero(self):
    hero_name = validate_input("Hero's name: ", str)
    hero = Hero(hero_name)
    add_item = None
    while add_item != '4':
      add_item = validate_input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ", str)      
      if add_item == '1':
        ability = self.create_ability()
        hero.add_ability(ability)
      elif add_item == '2':
        weapon = self.create_weapon()
        hero.add_weapon(weapon)
      elif add_item == '3':
        armor = self.create_armor()
        hero.add_armor(armor)
    return hero

  def build_team_one(self):
    team_name = validate_input("What's team one's name? : ", str)
    self.team_one = Team(team_name)
    num_of_team_members = int(validate_input(f"How many members would you like on {team_name}?\n", int))
    for i in range(num_of_team_members):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  def build_team_two(self):
    team_name = validate_input("What's team two's name? : ", str)
    self.team_two = Team(team_name)
    num_of_team_members = int(validate_input(f"How many members would you like on {team_name}?\n", int))
    for i in range(num_of_team_members):
      hero = self.create_hero()
      self.team_two.add_hero(hero)

  def team_battle(self):
    self.team_one.attack(self.team_two)

  def show_stats(self):
      print("\n")
      print(self.team_one.name + " statistics: ")
      self.team_one.stats()
      print("\n")
      print(self.team_two.name + " statistics: ")
      self.team_two.stats()
      print("\n")

      self.calculate_kd(self.team_one)
      self.calculate_kd(self.team_two)

      # Here is a way to list the heroes from Team One that survived
      team_1_live = self.list_survivors(self.team_one)
      team_2_live = self.list_survivors(self.team_two)

      if team_1_live > team_2_live: 
        print(f"{self.team_one.name} wins!")
      elif team_2_live > team_1_live: 
        print(f"{self.team_two.name} wins!")
      else:
        print("It's a tie!")


  def calculate_kd(self, team): 
    team_kills = 0
    team_deaths = 0
    for hero in team.heroes:
      team_kills += hero.kills
      team_deaths += hero.deaths
    if team_deaths == 0:
      team_deaths = 1
    print(team.name + " average K/D was: " + str(team_kills/team_deaths))

  def list_survivors(self, team):
    survivors = 0
    for hero in team.heroes:
      if hero.deaths == 0:
        survivors += 1
        print("survived from " + team.name + ": " + hero.name)
    return survivors

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
