class Product:
	def __init__(self, price, name, weight, brand, status="for sale"):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = status
	
	def tax_designation(self, tax=0.1):
		tax = int(self.price) * 0.1
		taxed = int(self.price) * 1.1
		self.tax = tax
		self.taxed = taxed
		return self
	
	def a(self):
		print(f"Subtotal: ${self.price}\nTax: ${self.tax} \nTotal: ${self.taxed}")
	
	def product_return(self,reason):
		self.tax_designation()
		print(f"The old price is ${self.price}. With tax, that's ${self.taxed}.")
		if reason == "defective":
			self.price = 0
			self.status = "defective"
			print(f"The new price is ${self.price} and the status is {self.status}.")
			return self.price, self.status
		elif reason == "opened":
			print(f"The old price is ${self.price}.")
			self.price = int(self.price)*0.8
			self.status = "opened"
			print(f"The new price is ${self.price} and the status is {self.status}.")
			return self.price, self.status
		elif reason == "like new":
			print("No change to price or status")
			return self
	
	def sale(self):
		if self.status == "for sale":
			self.tax_designation()
			self.a()
		if self.status == "opened":
			self.tax_designation()
			self.price = int(self.price)*0.8
			self.a()
		if self.status == "defective":
			print("I'm sorry, that's not for sale.")


eyeshadow = Product(52,"Naked 2",8,"Urban Decay")
facial_serum = Product(1115,"The Cure",0.4,"Guerlain")
foundation = Product(64,"Luminous Silk",1,"Armani","opened")
lipstick = Product(38,"Rouge pur Couture",1,"YSL","defective")
concealer = Product(32,"Touche Eclat",1,"YSL","for sale")
			
