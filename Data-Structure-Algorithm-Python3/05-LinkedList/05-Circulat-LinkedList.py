class Node:
	# constructor take data as argument and create new Node
	def __init__(self,data):
		self.data=data
		self.next=None

	def __str__(self):
		print(self.data,end="")
		return ""


class CircularList(object):
	
	def __init__(self):
		self.head=None

	# get count of all nodes	
	def size(self):
		current = self.head 
		length=0
		while current.next!=self.head:
			current=current.next
			length+=1

		return length+1

	# add new node to end of Node
	def add(self):
		item = input("\n\t Enter Element : ")
		new = Node(item)
		
		# if head is null make this node as Head Node 
		if not self.head:
			self.head=new
			# make new node to point to head node 
			new.next = self.head
			return
		# travel to last node . since it is circular list last node->next will point to start node	
		current=self.head
		while current.next!=self.head:
			current=current.next	

		# make previous node next point to the new node 
		current.next=new
		# make new node to point to head node 
		new.next=self.head 
			
	# remove node from head
	def remove(self):
		current = self.head
		
		# if list is empty
		if self.isEmpty():
			print(" !!! LinkedList is Empty !!! ")

		# if current item is only node in List 
		elif self.head.next==self.head:
			print(" Deleted ",current.data," from List ")
			del self.head
			self.head = None

		else:
			while current.next!=self.head:
				# to store new last node address
				prev=current
				current=current.next
				
			print(" Deleted ",current.data," from List ")
			del current
			# point new last node next to first node
			prev.next=self.head 

	def isEmpty(self):
		if self.head==None:
			return True
		return False			

	def display(self):

		current=self.head
		# If no Item in Linked List
		if self.isEmpty():
			print(" !!! Linked List is Empty !!!")
			return

		else:
			while (current.next!=self.head):
				print(current,"=>",end=" ")
				current=current.next
		# print last node
		print(current)	

	def getMid(self):
		
		if self.head==None or self.head.next==self.head:
			return False,

		fast=self.head
		slow=self.head
		prev=slow
		
		while True:
			prev=slow
			slow=slow.next
			fast=fast.next.next
			if fast==self.head or fast.next==self.head:
				break

		return True,prev,slow	
			

def mainMenu():
	
	while True:	
		print("\n ******* Menu ******* ")
		print("\n\t 1) Add \n\t 2) Remove \n\t 3) Display  \n\t 4) Size \n\t 5) Mid ")
		print(" \t 6) Exit",end="\t\t")
		choice = eval(input("Enter the Option : "))
		
		# Add Item to the end of Linked List
		if choice == 1:			
			cl.add()
		
		# Remove Item from Linked List
		elif choice == 2:
			cl.remove()
		
		# Traverse Linked List 	
		elif choice == 3:
			cl.display()
			
		# size			
		elif choice == 4:
			print(" LinkedList  Size is : ",cl.size())				
		
		elif choice == 5:
			result = cl.getMid()
			if result[0]:
				print("Prev Of Middle : ",result[1])	
				print(" Middle : ",result[2])	
			else:
				print(" No Middle ")	
		elif choice == 6 : break
		
		else:
			print(" %% $$ ## Enter valid Option !! !! !!")

cl = CircularList()

if __name__ == '__main__':
	mainMenu()

