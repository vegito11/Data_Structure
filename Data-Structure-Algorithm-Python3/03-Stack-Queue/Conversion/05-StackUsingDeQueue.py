# Stack using 1 Dequeue
# push O(1) pop O(1)

class Stack:
	
	def __init__(self):
		self.dequeue = []

	def size(self):
		return len(self.dequeue) 

	def isEmpty(self):
		return len(self.dequeue) == 0

	def push(self,item):
		self.dequeue.append(item)

	def pop(self)	:
		if self.isEmpty():
			print(" !!! Stack is Underflow !!! ")
		else:
			print(self.dequeue.pop())

st = Stack()

st.push(10)
st.push(20)
st.push(30)
st.push(40)

print(st.size())
print(st.isEmpty())

st.pop()
st.pop()