class Node:
	# constructor take name and age as argument and create new Node
	def __init__(self,data):
		self.data=data
		self.next=None

	def __str__(self):		
		return f'{self.data}'

class LinkedList(object):
	
	def __init__(self):
		self.head=None

	# get count of all nodes	
	def size(self):
		current = self.head 
		length=0
		while current:
			current=current.next
			length+=1

		return length	
	
	# add new node to head
	def add(self,data):
		
		new = Node(data)
		# if head is null make this node as Head Node 
		if not self.head:
			self.head=new
		# Insert this node as first Node
		else:
			new.next= self.head 
			self.head=new
	
	# remove node from head
	def remove(self):
		current = self.head
		
		# if list is empty
		if self.isEmpty():
			print(" !!! LinkedList is Empty !!! ")

		# if current item is only node in List 
		elif self.head.next==None:
			print(" Deleted ",current.data," from List ")
			del self.head
			self.head = None

		else:
			self.head=current.next
			print(" Deleted ",current.data," from List ")
			del current

	# is List is Empty ? 		
	def isEmpty(self):
		if self.head==None:
			return True
		return False			

	# Display List 
	def display(self):

		# If no Item in Linked List
		if self.isEmpty():
			print(" !!! Linked List is Empty !!!")

		else:
			current=self.head
			while (current!=None):
				print(current,end=" ")
				current=current.next
			print()

	# find out list is even or odd lenght without counting size		
	def oddOrEven(self):
		print("_"*30)
		result = "ODD"

		# if onyl one node in List
		if self.head.next==None:
			return result
		# will move only step
		slow = self.head
		# will move two step
		fast = self.head

		while True:

			# then it will be even list	 ** Remember fast.next will result in None.next 
			if fast == None	:
				return "Even"

			# then it will odd list
			if fast.next == None:
				return result

			slow = slow.next
			fast=fast.next.next

		return result

ll = LinkedList()
ll.add(10)
print(ll.oddOrEven())
ll.add(20)
print(ll.oddOrEven())
ll.add(30)
print(ll.oddOrEven())
ll.remove()
print(ll.oddOrEven())
