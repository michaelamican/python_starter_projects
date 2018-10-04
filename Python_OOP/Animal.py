class Animal:
	def __init__(self, name="beast", health=100):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		walk = self.health
		return self
	def run(self):
		self.health -= 5
		run = self.health
		return self
	def display_health(self):
		print(self.health)
		return self

class Dog(Animal):
	def __init__(self):
		super().__init__()
		self.health = 150
	def pet(self):
		self.health += 5
		pet = self.health
		return self

class Dragon(Animal):
	def __init__(self):
		super().__init__()
		self.health = 150
	def fly(self):
		self.health += 10
		fly = self.health
		return self
	def display_health(Animal):
		print("I am a Dragon")

class Monkey(Animal):
	def __init__(self):
		super().__init__()
		self.health = 130
	def dance(self):
		self.health += 10
		dance = self.health
		print("Bananananananana")
		return self


Lassie = Dog()
Spyro = Dragon()
George = Monkey()

George.pet()
George.fly()
George.dance().display_health()

Lassie.display_health().fly()

