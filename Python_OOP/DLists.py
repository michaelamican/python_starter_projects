class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class DList(Node):
	def __init__(self,value):
		node = Node(value)
		self.head = node
	def list_prepend(self,value):
		node = Node(value)
		value.prev = node
		if(node.next == None):
			value.next = None
			list.lastNode = value
		else:
			value.next = node.next
			node.next.prev = value
		node.next = value
	def start_this_off(self,value):
		node = Node(value)
		if(list.Node == None):
			list.first = first_value
			first.next = None
		else:
			list_prepend(list, list.first, newNode)
	def move_forward(self,value):
		node = Node(value)
		runner = self.head
		while(runner.next.value != None):
			runner = runner.next
	def move_back(self,value):
		node = Node(value)
		runner = self.head
		while(runner.prev.value !=None):
			runner = runner.prev
	def strike_node(self,value):
		node = Node(value)
		if(node.prev == None):
			list.first = node.next
		else:
			node.prev.next = node.next
		if(node.next == None):
			list.last = node.prev
		else:
			node.next.prev = node.prev
	def print_values(self, msg=""):
		node = Node(value)
		runner = self.head
		while(runner.next != None):
			print(id(runner), runner.value, id(runner.next))
			runner = runner.next
			print(id(runner), runner.value, id(runner.next))