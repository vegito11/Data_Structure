class Stack(object):
	""" Stack Class which perform all operations of Stack """
	
	def __init__(self):
		super(Stack, self).__init__()
		self.items = []

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def peek(self):
		# if Stack is empty
		if self.isEmpty(): 
			return " Stack Is Underflow "
		else:
			# return self.items[-1]
			return self.items[self.size()-1]

	def push(self,item):
		self.items.append(item)	

	def pop(self):
		if self.isEmpty():
			return " Stack Is Underflow "
		return self.items.pop()


