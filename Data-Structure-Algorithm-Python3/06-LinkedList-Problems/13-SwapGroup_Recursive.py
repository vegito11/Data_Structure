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

	def display(self):

		if self.head==None: return None
		else:
			current=self.head
			while (current!=None):
				print(current,"=>",end=" ")
				current=current.next
			print("NULL")

	@staticmethod
	def swapGroupNodes(current,k=2):

		if current==None:
			return None
		# if k is negative number	
		if k<=0:
			return current	

		# Initialize prev and future variable
		future=prev=None						
		# count will help to reverse link until group size
		cnt=0

		####### Initiallization Finished Above ######
		# newgroup initial start             
		prevGroupEnd = current  # become End After reversal

		# reverse links of the group (same step of reverse LL)
		while current !=None and cnt!=k:
		
			# store for next iteration
			future = current.next
			# current point to previous Node (reverse Link)
			current.next=prev
		
			# store previous as current node
			prev = current
			# current will point to next node in iteration
			current=future
			cnt+=1
		
		# this function will return new List which os reversed	
		prevGroupEnd.next= LinkedList.swapGroupNodes(current,k)
		print(prev)
		return prev	

	def swapNodes(self,k):
		# new Start of LinkedList is returned by this function
		self.head = self.swapGroupNodes(self.head,k)
			
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.add(60)	
ll.display()
ll.swapNodes(3)
ll.display()
# print(ll.head)
# print(ll.head.next)

"""
	K = 3
	---------------------------------------------
	CASE 1 : length is less that k 
			 10=>20=>None

	CASE 2 : length is equal to  k 
			 10=>20=>30=>None
	
	CASE 3 : EVEN
			 10=>20=>30=>40=>50=>60=>None
			 30=>20=>10=>60=50=>40=>None
	
	CASE 4: ODD
			10=>20=>30=>40=>50=>60=>70=>80=>90=>100=>None
			30=>20=>10=>60=>50=>40=>90=>80=>70=>100=>None

	STEPS : 
		
		1) store starting of group(without Reversal)
		2) reverse linked list of size K 
		
		3) if first reversal then New Start is this group Start
		
		4) Previous Iteration Starting next will point to newly reversed Linked List
		5) store starting of this List for next Iteration

"""