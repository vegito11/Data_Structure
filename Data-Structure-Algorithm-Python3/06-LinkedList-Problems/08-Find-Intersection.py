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

	# return two List Head which are Interseting each other		
	@staticmethod		
	def makeInterectionList():
		
		# head of first Linked List 
		l1 = LinkedList()
		l1.add(40)
		l1.add(30)
		l1.add(20)
		l1.add(10)

		# attach this linked list at end of each linked list 
		l3 = LinkedList()
		l3.add(55)
		l3.add(66)
		l3.add(77)

		# head of second Linked List 
		l2 = LinkedList()
		l2.add(22)
		l2.add(11)
		
		# display first list
		l1.display()
		# display second list
		l2.display()
		# display third list
		l3.display()
		print("------ After Intersetion ----- ")
		
		# add 3rd list at end of First List
		current=l1.head
		# traverse List till the End
		while current.next!=None:
			current=current.next
		# last node .next will contain address of third list start node 
		current.next=l3.head
		
		l1.display()	
		
		######==============================

		# add 3rd list at end of Second List
		current=l2.head
		# traverse List till the End
		while current.next!=None:
			current=current.next
		# last node .next will contain address of third list start node 
		current.next=l3.head
		
		l2.display()
		print("-"*30)
		return l1,l2

	# head1=10->20->30->40- --->55->66->77
	# head2=11->22- --->50->60->70	
	@staticmethod	
	def findInterection(list1,list2):
		"""
		1) find length of both list 
		2) find difference between (Diff=D) two list length 
		3) Move larger List D Step Ahead
		4) Mode two list until they reach to same node
		"""
		len1 = list1.size()
		len2 = list2.size()
		print("length of List 1 : ",len1)
		print("length of List 2 : ",len2)

		# if first List is larger in length
		if len1>len2:
			# find out length difference of two List
			diff = len1-len2
			# current will store first node head address
			currentOne=list1.head

			# move first LIST diff STEPS ahead
			while diff!=0:
				currentOne=currentOne.next
				diff-=1
			# print(currentOne)

			# store second LIST head address for traversing
			currentSecond=list2.head
			# if any of node reach at end or both node reach at intersction Stop
			while currentOne and currentSecond and currentOne!=currentSecond:
				# move first list one step ahead
				currentOne=currentOne.next
				# move second list one step ahead
				currentSecond=currentSecond.next
		
		# if second List is larger in length or both of same length
		else:
			# find out length difference of two List
			diff = len2-len1
			
			# current will store second node head address
			currentSecond=list2.head

			# move Second List diff STEPS ahead
			while diff!=0:
				currentSecond=currentSecond.next
				diff-=1
			# print(currentSecond)

			# store First LIST head address for traversing
			currentOne=list1.head
			# if any of node reach at end or both node reach at intersction Stop
			while currentOne and currentSecond and currentOne!=currentSecond:
				# move first list one step ahead
				currentOne=currentOne.next
				# move second list one step ahead
				currentSecond=currentSecond.next
		
		return currentOne

# destruct tuple
head1,head2 =  LinkedList.makeInterectionList()

# print(LinkedList.findInterection.__doc__)

# intersctionNode = LinkedList.findInterection(head1,head2)
intersctionNode = LinkedList.findInterection(head2,head1)

print(" Two LinkedList list Intersect At : ",intersctionNode)
