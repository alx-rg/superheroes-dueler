# source env/bin/activate
# pip3 install -r requirements.txt
import random

class Hero:
	def __init__(self, name, starting_health=100):
		self.name = name
		self.starting_health = starting_health
		self.current_health = starting_health

	def fight(self, opponent):
		winner = random.choice([self, opponent])
		print(f"{winner.name} wins!")
		return winner

if __name__ == "__main__":

   my_hero = Hero('Pinky and the Brain', 250)
   my_hero2 = Hero('Jimmy Neutron', 300)
   print(my_hero.name)
   print(my_hero.current_health)
   my_hero.fight(my_hero2)
