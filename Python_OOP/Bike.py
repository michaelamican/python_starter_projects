class Bike:
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print(f"I am a bike with {self.miles} miles. I top out at {self.max_speed}, and am yours for only ${self.price}!")
		return self
	def ride(self):
		if self.miles < 0:
			self.miles *= (-1)
		print("Riding "+str(self.miles)+" miles")
		int(self.miles) += 10
		return self
	def reverse(self):
		print(f"Mileage: {self.miles}.")
		print("Reversing...")
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		print(f"New mileage: {self.miles}")
		return self

schwinn = Bike(375,38,120)
bugatti = Bike(850,30,1309)
armani = Bike(1800,28,3)

schwinn.ride().ride().ride().reverse().displayInfo()
bugatti.ride().ride().reverse().reverse().displayInfo()
armani.reverse().reverse().reverse().displayInfo()
