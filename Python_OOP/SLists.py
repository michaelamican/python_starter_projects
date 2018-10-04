class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class SList:
	def __init__(self,value):
		node = Node(value)
		self.head = node
	def addNode(self,value):
		node = Node(value)
		runner = self.head
		while(runner.next != None):
			runner = runner.next
		runner.next = node
	def removeNode(self,value):
		runner = self.head
		if(self.head.value == value):
			self.head = runner.next 
		while(runner.next.value != value):
			runner = runner.next
			if(runner.next.value == value):
				runner.next = runner.next.next
				return True
		return False
	def printAllValues(self, msg=""):
		runner = self.head
		print("\n\head points to ", id(self.head))
		print("Printing the values in the list ---", msg, "---")
		while(runner.next != None):
			print(id(runner), runner.value, id(runner.next))
			runner = runner.next
		print(id(runner), runner.value, id(runner.next))
    




print("\n\n\n\n========START OF THE PROGRAM========\n\n\n\n")


list.printAllValues("Attempt 1")