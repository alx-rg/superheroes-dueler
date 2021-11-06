class Animal:
  def __init__(self, name, sleep_duration, legs):
    self.name = name
    self.sleep_duration = sleep_duration
    self.legs = legs

  def sleep(self):
    print(f"{self.name} sleeps for hours {self.sleep_duration}")
   


# Note that the class Dog takes in Animal as a parameter!
class Dog(Animal):
  def bark(self):
    print("Woof! Woof!")
  def movement(self):
      print(f'{self.name} moves on {self.legs} appendages.')     


""" class Doggo:
   def __init__(self, name, breed):
      self.name = name
      self.breed = breed
      print('dog initialized!')
   
   def bark(self):
      print('Woof! Woof! Happy')

 """

my_dog = Dog("Sophie", 12, 4)
my_dog.sleep()
my_dog.bark()
my_dog.movement()
