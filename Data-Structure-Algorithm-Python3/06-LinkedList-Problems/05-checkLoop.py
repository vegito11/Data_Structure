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

	# Make one List and make its end to point any random Node
	def makeLoop(self):
		self.add(70)
		self.add(60)
		self.add(50)
		self.add(40)
		self.add(30)
		self.add(20)
		self.add(10)
		self.display()
		current= self.head
		# Make last node point to 40
		print(self.head.next.next.next)

		# Travel till last node
		while (current.next!=None):
			current=current.next			
		
		# Make a loop by pointing last node to 40 node
		current.next = self.head.next.next.next

		# self.display()

	def makeList(self):
		self.add(60)
		self.add(50)
		self.add(40)
		self.add(30)
		self.add(20)
		self.add(10)
		# self.display()		

	# detect a loop 
	def detectLoop(self):
		
		# if list is empty or only one node in the List
		if not self.head or self.head.next==None:
			return False
		
		# make two pointer one is moving one step and another is moving two step at a time
		fast = slow = self.head

		while True:
			# if there is no loop there will not be a point where we reach to None
			if fast == None or fast.next==None :
				return (False,)
			
			# if loop then then this conditon will be true 
			if slow==fast and slow!=self.head:
				return True,slow 
			# move by one step 
			slow= slow.next	
			# move by two step
			fast= fast.next.next


		return False

ll = LinkedList()
ll.makeLoop()
# ll.makeList()
result = ll.detectLoop()

if result[0] == False:
	print(" !!! There is no loop in Linked List !!! ")
else:
	print(" There is a Loop in Linked List !! ")	

