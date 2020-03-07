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
		# Insert this node as last Node
		else:
			current=self.head
			while current.next!=None:
				current=current.next

			current.next=new	
	
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

	def swapNodes(self):
		# if List is empty or only one Node in List
		if self.head==None or self.head.next==None:
			return self.head
		# make second node as new Start	
		newStart=self.head.next	
		# start from First Node
		oldFirst=self.head

		# 10->20->None(newPair)
		# 10->20->-30(newPair)->None
		while True:
			
			# this second Node which is going to be new First of Pair (20)
			newFirst = oldFirst.next
			
			# this node will be new Pair Start (30)
			newPair=newFirst.next

			# now Reverse Link (10<=20)
			newFirst.next=oldFirst

			# if Even or ODD Breaking condition
			if newPair == None or newPair.next==None:
				# newPair can be None or only last node remaining
				oldFirst.next=newPair
				break;

			# (40) store so that we can able to point old next to it 10-=>40
			newPairSecond = newPair.next

			# now oldFirst will point to newPair SECOND which will become FIRST (10=>40)
			oldFirst.next=newPairSecond

			# Now repeat this Process for next pair (30=>40)
			oldFirst=newPair

		self.head=newStart
		return newStart	

			
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.add(60)	
ll.display()

ll.swapNodes()
ll.display()

"""
	A) EVEN
		10=>20=>30=>40=>50=>60=>None
		20=>10=>40=>30=>60=>50=>None
	B) ODD 
		10=>20=>30=>40=>50=>None
		20=>10=>40=>30=>50=>None

	1) NEW Start will be 20 
	
	2) In Each Step this will performed
		a) Reverse Link : 2nd.next Will point to First 
		b) Old First Next : First Next will Point to (new First of next PAIR)
	
	3) break condition : 




"""