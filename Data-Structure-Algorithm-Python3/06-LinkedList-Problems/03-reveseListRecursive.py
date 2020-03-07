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

	# reverse a List 
	# 10->20->30->40->
	#  <-10<-20
	#  <-20<-30
	#  <-30<-40
	# head = 40
	def _reverse(self,first):
		"""
			In this approach of reversing a linked list by passing a single pointer what we 
			are trying to do is that 
			1) we are making the previous node of the current node as his next node to 
			   reverse the linked list.
			2) We return the pointer of next node to his previous(current) node and 
			   then make the previous node as the next node of returned node and then 
			   returning the current node.
			3) We first traverse till the last node and making the last node as the head node of
			   reversed linked list and then applying the above procedure in the recursive manner.
		"""
		# If List is Empty
		if first==None:
			print(" List is Empty ")
			return None

		# when it will reach to 40 it will break
		# so Here breaking condition is last Node of List .
		if first.next==None:
			return first

		# from here processing will start that is 	
		# first will 30 and second will be 40	
		second = self._reverse(first.next)
		# print(second) It wil be always 40 
		first.next.next = first
		# second.next = first

		# It will changed in next step (30.next=None)(30 will become second)
		first.next=None

		# 40 will be returned as result at each recursion
		return second

	def reverseList(self):
		self.head = self._reverse(self.head)

ll = LinkedList()
ll.add(40)
ll.add(30)
ll.add(20)
ll.add(10)
ll.display()

ll.reverseList()
ll.display()

