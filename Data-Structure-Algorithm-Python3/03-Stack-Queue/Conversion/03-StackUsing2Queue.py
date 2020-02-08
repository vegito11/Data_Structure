# Stack using 2 Queue
# making push as expensive
# pop O(1)

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

	# enqueue new Item in Queue to whichQueue
	# change whichQueue
	# dequeue all item from otherQueue to whichQueue
	def push(self,item)	:
		
		if self.whichQueue == 1:
			# Insert new Item in que1
			self.que1.append(item)
			self._changeQueue()
			# remove all item from Queue2 to Queue1
			while len(self.que2):
				self.que1.append(self.que2.pop(0))

		elif self.whichQueue == 2:
			
			# Insert new Item in self.que2
			self.que2.append(item)
			self._changeQueue()

			# remove all item from Queue1 to Queue2
			while len(self.que1):
				self.que2.append(self.que1.pop(0))


	# pop is O(1) dequeue from 	
	def pop(self):
		if self.isEmpty():
			print(" !!! Stack is Underflow !!! ")
		
		elif self.whichQueue == 2:
			print(self.que1.pop(0))
		else:	
			print(self.que2.pop(0))
	
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