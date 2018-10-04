class Car:
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
	def tax_designation(self):
		if self.price > 100000:
			tax = 0.15
		else:
			tax = 0.12
		self.tax = tax
		return self
	def display_all(self):
		self.tax_designation()
		print(f"Price: {self.price}\nSpeed: {self.speed}\nFuel: {self.fuel}\nMileage: {self.mileage}\nTax rate: {self.tax}%")

prius = Car(9999,100,'full',12000)
kia = Car(12000,150,'empty',9000)
maserati = Car(150000,220,'half-empty',0) 
rolls = Car(750000,180,'half-full',1300)
tesla = Car(32000,190,'electric',700)
impala = Car(3500,80,'sludgy',350000)