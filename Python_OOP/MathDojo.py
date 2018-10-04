class MathDojo:
	def __init__(self, *nums):
		self.num = 0
	def add(self,*nums):
		for i in nums:
			self.num += i
		return self
	def subtract(self,*nums):
		for i in nums:
			self.num -= i
		return self



md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2)
print(x) # should print 5