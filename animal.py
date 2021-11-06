class Animal:
  def __init__(self, eat, drink, name):
    self.eat = eat
    self.drink = drink
    self.name = name

  def eating(self):
    print(f'{self.name} is eating')

  def drinking(self):
    print(f'{self.name} is drinking.') 

class Frog(Animal):

  def jumping(self):
    print(f'{self.name} is jumping.')
    

cow = Animal('food', 'water', 'jimmy')
cow.eating()
cow.drinking()

frog = Frog('grubs', 'lilys', 'pumper')
frog.jumping()
frog.eating()
frog.drinking()
