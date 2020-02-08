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


def operation():
	st = Queue()

	while True:
		print("\n ******* Menu ******* ")
		print("\n\t 1) Enqueue \n\t 2) Dequeue \n\t 3) isEmpty \n\t 4) Size \n\t 5) Exit",end="\t\t")
		choice = eval(input("Enter the Option : "))
		print()
		
		# Enqueue
		if choice == 1:
			item = input("\n\t Enter Element : ")
			st.enqueue(item)
		
		# dequeue	
		elif choice == 2:
			item = st.dequeue()
			try:
				int(item)
				print(item," Removed from Queue")
			except Exception as e:
				print(item)

		# isEmpty
		elif choice == 3:
			print(st.isEmpty())
	
		# size			
		elif choice == 4:
			print("Queue Size is : ",st.size())				
		
		elif choice == 5 : break
		
		else:
			print(" !!! Please Enter Valid Option !!!! ")
			


if __name__ == '__main__':
	operation()

