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

	def reverseList(self):
		# if only one node in List or List is Empty
		if self.head==None or self.head.next == None:
			return;
		# 10->20->30->40->None	
		else:	
			prev=None
			current=self.head
			future = current
			while current !=None:
				# store for next interation
				future = current.next
				# current point to previous Node (reverse Link)
				current.next=prev
				# store previous as current node
				prev = current
				# current will point to next node in interation
				current=future
			
			self.head = prev	


ll = LinkedList()
ll.add(40)
ll.add(30)

ll.reverseList()
ll.display()

ll.add(20)
ll.add(10)
ll.display()

ll.reverseList()
ll.display()

