# Queue using 2 Stack 
# by making dequeue expensive 
# by making enqueue O(1) first element always at top

class Queue:
 	
 	def __init__(self):
 		self.inStack = []
 		self.outStack = []

 	# Always insert item in First Stack(InStack)
 	def enqueue(self,item):
			self.inStack.append(item)

 	# if OutStack Not Empty Pop  from outStack Else :
 	# remove all items from inStack to outStack 
 	# Pop First Item from outStack

 	def dequeue(self):
 		
 		# If no element in any of the stack
 		if len(self.outStack)==0 and len(self.inStack) == 0:
 			print(" !!! Queue in Empty !!! ") 	
 			return

 		# if Outstack is not empty pop from outstack:
 		if len(self.outStack) !=0:
 			print(self.outStack.pop())
 			return

 		else:
 			
 			while len(self.inStack)!=0:
 				self.outStack.append(self.inStack.pop())

 				
 		print(self.outStack.pop())
 		return
 	
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
que.enqueue(40)
que.enqueue(50)
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()

que.size()