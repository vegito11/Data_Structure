class Dequeue(object):
	""" Dequeue Class which perform all operations of Dequeue """
	
	def __init__(self):
		super(Dequeue, self).__init__()
		self.items = []

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def addFront(self,item):
		self.items.insert(0,item)	

	def addRear(self,item):

		self.items.append(item)	

	def removeFront(self):
		if self.isEmpty():
			return " Queue is UnderFlow"
		return self.items.pop(0)	

	def removeRear(self):
		if self.isEmpty():
			return " Queue is UnderFlow"
		return self.items.pop()


def operation():
	st = Dequeue()

	while True:
		print("\n ******* Menu ******* ")
		print("\n\t 1) addFront \n\t 2) addRear \n\t 3) removeFront \n\t 4) RemoveRear" ,end="")
		print("\n\t 5) isEmpty \n\t 6) Size \n\t 7) Exit",end="\t\t")
		choice = eval(input("Enter the Option : "))
		print()
		
		# addFront
		if choice == 1:
			item = input("\n\t Enter Element : ")
			st.addFront(item)
		
		# addRear
		elif choice == 2:
			item = input("\n\t Enter Element : ")
			st.addRear(item)
		
		# removeFront
		elif choice == 3:
			item = st.removeFront()
			try:
				int(item)
				print(item," Removed from Queue")
			except Exception as e:
				print(item)

		# removeRear
		elif choice == 4:
			item = st.removeRear()
			try:
				int(item)
				print(item," Removed from Queue")
			except Exception as e:
				print(item)

		# isEmpty
		elif choice == 5:
			print(st.isEmpty())
	
		# size			
		elif choice == 6:
			print("Queue Size is : ",st.size())				
		
		elif choice == 7 : break
		
		else:
			print(" !!! Please Enter Valid Option !!!! ")
			


if __name__ == '__main__':
	operation()
	pass
