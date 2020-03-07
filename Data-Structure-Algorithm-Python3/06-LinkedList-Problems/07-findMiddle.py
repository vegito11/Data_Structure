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

	# get middle element of list
	def getMid(self):		
		fast = self.head
		slow = self.head
		# if list is empty
		if self.head==None:
			return False,
		# if list contain only one node	
		if self.head.next==None:
			return False,

		# if fast node is reach to last next or fast pointer reach to last node
		while fast and fast.next:
			prev = slow
			slow	= slow.next
			fast	= fast.next.next

		return True,slow,prev	
			
ll = LinkedList()
ll.add(90)
ll.add(80)
ll.add(70)
ll.add(60)
ll.add(50)
ll.add(40)
# ll.add(30)
ll.display()
result = ll.getMid()
print(result[0])

if result[0]==True:
	print(" Previous of Middle Element : ",result[2])
	print(" Middle Element : ",result[1])

