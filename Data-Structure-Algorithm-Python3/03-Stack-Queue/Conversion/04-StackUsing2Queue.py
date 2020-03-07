# Stack using 2 Queue
# making pop as expensive
# push O(1)

class Stack:
	
	def __init__(self):
		self.que1 = []
		self.que2 = []
		# indicate in which queue to push new Item
		self.whichQueue=1

	def size(self):
		return len(self.que1) + len(self.que2)

	def isEmpty(self):
		return len(self.que1) + len(self.que2) == 0

	# dequeue all items(n-1) from WhichQueue to OtherQueue 
	# Dequeue Last remainingm from WhichQueue
	# change whichQueue
	def pop(self)	:
		if self.isEmpty():
			print(" !!! Stack is Underflow !!! ")

		# which queue is pointing to current insert Queue which is Queue1	
		if self.whichQueue == 1:
			
			while len(self.que1)!=1:
				self.que2.append(self.que1.pop(0))
			print(self.que1.pop(0))
			self._changeQueue()
			return

		if self.whichQueue == 2:
			while len(self.que2)!=1:
				self.que1.append(self.que2.pop(0))
			print(self.que2.pop(0))
			self._changeQueue()
			return

	# pop is O(1) dequeue from 	
	def push(self,item):
		
		if self.whichQueue == 1:
			self.que1.append(item)
		elif self.whichQueue == 2 :	
			self.que2.append(item)
	
	# changeQueue 1 to 2 or 2 to 1	
	def _changeQueue(self):
		
		if self.whichQueue==1:
			self.whichQueue=2
		
		else:
			self.whichQueue=1

st = Stack()

st.push(10)
st.push(20)
st.push(30)
st.push(40)

print(st.size())
print(st.isEmpty())

st.pop()
st.pop()