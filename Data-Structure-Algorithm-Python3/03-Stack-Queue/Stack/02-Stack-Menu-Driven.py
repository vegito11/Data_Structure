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


def operation():
	st = Stack()

	while True:
		print("\n ******* Menu ******* ")
		print("\n\t 1) Push \n\t 2) Pop \n\t 3) Peek  \n\t 4) isEmpty \n\t 5) Size \n\t 6) Exit",end="\t\t")
		choice = eval(input("Enter the Option : "))
		print()
		
		# Push
		if choice == 1:
			item = input("\n\t Enter Element : ")
			st.push(item)
		
		# Pop	
		elif choice == 2:
			item = st.pop()
			try:
				int(item)
				print(item," Removed from Stack")
			except Exception as e:
				print(item)
		
		# Peek	
		elif choice == 3:
			item = st.peek()
			try:
				int(item)
				print(item," Removed from Stack")
			except Exception as e:
				print(item)			
			
		# isEmpty
		elif choice == 4:
			print(st.isEmpty())
	
		# size			
		elif choice == 5:
			print("Stack Size is : ",st.size())				
		
		elif choice == 6 : break
		
		else:
			print(" !!! Please Enter Valid Option !!!! ")
			


if __name__ == '__main__':
	operation()

