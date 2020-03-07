# Queue using 2 Stack 
# by making enqueue expensive 
# by making dequeue O(1) first element always at top
#  When we pop order become reverese
class Queue:
 	
 	def __init__(self):
 		self.inStack = []
 		self.outStack = []

 	# remove all items from inStack to outStack 
 	# insert New Item to inStack 
 	# outStack to Instack 
 	def enqueue(self,item):
 		
 		while len(self.inStack)!=0:
 			self.outStack.append(self.inStack.pop())

 		self.inStack.append(item)

 		while len(self.outStack)!=0:
 			self.inStack.append(self.outStack.pop())

 	# remove item from Instack		
 	def dequeue(self):
 		if len(self.inStack) == 0:
 			print(" !!! Queue in Empty !!! ") 	
 			return		
 		print(self.inStack.pop())
 	
 	def size(self):
 		print("Size is : ",len(self.inStack))
 	

 	def isEmpty(self):
 		# If any of the list contain element return True 
 		if len(self.inStack) or len(self.outStack):
 			return False
 		return True	
que = Queue()

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.size()

que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.enqueue(30)
que.dequeue()

que.size()