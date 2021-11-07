# source env/bin/activate
# pip3 install -r requirements.txt
import random

from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
	def __init__(self, name, starting_health=100):
		self.abilities = list()
		self.armors = list()
		self.deaths = 0
		self.kills = 0

    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
		# name of hero goes below		
		self.name = name
		self.starting_health = starting_health
		self.current_health = starting_health

	def fight(self, opponent):
		if (len(self.abilities) == 0) and (len(opponent.abilities) == 0):
			print("Neither Heroes have abilities, it's a draw")
			opponent.current_health = 0
			self.current_health = 0
		else:
			while True:
				attack_damage = self.attack()
				opponent_attack_damage = opponent.attack()
				self.take_damage(opponent_attack_damage)				
				opponent.take_damage(attack_damage)
				if not self.is_alive() and not opponent.is_alive():
						print("They both knocked each other out, it's a draw!")
						self.add_death(1)
						opponent.add_death(1)
						break											
				elif not opponent.is_alive():
					opponent.add_death(1)
					self.add_kill(1)
					print(f'{self.name} won! And beat the crap out of {opponent.name}!')
					break
				elif not self.is_alive():
					opponent.add_kill(1)
					self.add_death(1)
					print(f'{opponent.name} won! And beat the snot out of {self.name}!')
					break
					


	def add_kill(self, num_kills):
		self.kills += num_kills

	def add_death(self, num_deaths):
		self.deaths += num_deaths

	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		total_damage = 0
		for ability in self.abilities:
			total_damage += ability.attack()
		return total_damage

	def add_armor(self, armor):
		self.armors.append(armor)

	def defend(self):
		total_block = 0
		for armor in self.armors:
			total_block += armor.block()
		return total_block

	def add_weapon(self, weapon):
		self.abilities.append(weapon)

	def take_damage(self, damage):
		damage_total = self.defend()
		damage_took = max(damage - damage_total, 0)
		self.current_health -= damage_took


	def is_alive(self):
		if self.current_health <= 0:
			return False
		else:
			return True


		""" 
		#Damage and health 	
		def take_damage(self, damage):
		defence = self.defend()
		attack = self.attack()
		if attack > defence:
			damage = attack - defence
		else:
			damage = 0
		self.current_health -= damage
		return self.current_health 
		"""




if __name__ == "__main__":
	# If you run this file from the terminal
	# this block of code is executed.
	#hero = Hero("Wonder Woman")
	#weapon = Weapon("Lasso of Truth", 90)
	#hero.add_weapon(weapon)
	#print(hero.attack())


	 	
  #part 3
	hero1 = Hero("Wonder Woman")
	hero2 = Hero("Dumbledore")
	ability1 = Ability("Super Speed", 300)
	ability2 = Ability("Super Eyes", 130)
	ability3 = Ability("Wizard Wand", 10)
	ability4 = Ability("Wizard Beard", 20)
	hero1.add_ability(ability1)
	hero1.add_ability(ability2)
	hero2.add_ability(ability3)
	hero2.add_ability(ability4)
	hero1.fight(hero2)
	



	""" 
	hero = Hero("Grace Hopper", 200)
	hero.take_damage(150)
	print(hero.is_alive())
	hero.take_damage(15000)
	print(hero.is_alive())
 """

	
	""" 	
	hero = Hero("Grace Hopper", 200)
	shield = Armor("Shield", 50)
	hero.add_armor(shield)
	hero.take_damage(50)
	print(hero.current_health)
 	"""

	""" 
	ability = Ability("Great Debugging", 50)
	another_ability = Ability("Smarty Pants", 90)
	armor1 = Armor('spoon', 30)
	another_armor = Armor('glasses', 60)
	hero = Hero("Grace Hopper", 200)
	hero.add_ability(ability)
	hero.add_ability(another_ability)
	hero.add_armor(armor1)
	hero.add_armor(another_armor)
	print('attack')
	print(hero.attack())
	print('defend')
	print(hero.defend())
	print('health')
	print(hero.take_damage(110))
	print(hero.current_health)
 """


	"""    
	 my_hero = Hero('Pinky and the Brain', 250)
   my_hero2 = Hero('Jimmy Neutron', 300)
   print(my_hero.name)
   print(my_hero.current_health)
   my_hero.fight(my_hero2) 
	 """
