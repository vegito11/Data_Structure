class Queue(object):
	""" Queue Class which perform all operations of Queue """
	
	def __init__(self):
		super(Queue, self).__init__()
		self.items = []

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)	

	def dequeue(self):
		if self.isEmpty():
			return " Queue Is Empty "
		return self.items.pop()

