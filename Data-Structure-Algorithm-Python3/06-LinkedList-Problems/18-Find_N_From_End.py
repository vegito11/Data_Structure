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

	# add new node to at the end of list
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

	# 10=>20=>30=>40=>50=>60=>70
	# Get Nth Node from End List 
	def NthFromEnd(self,pos):
		# store first node address in this variable
		current=self.head
		# if only one node in List 
		if current==None or current.next==None:
			print("Less than 2 element in List ")

		# start from first Node	
		fast_traveler = current
		
		# for travelling first nth Node from Start<	
		for x in range(1,pos):
			# Move by one step
			fast_traveler=fast_traveler.next
			# if given position is Greater than Size of List return Empty
			if fast_traveler==None:return
		
		# print(fast_traveler)

		# Move One pointer from Start and another from Offset by one Step
		# until offset pointer reaches to end 
		while(fast_traveler.next!=None):
			# move one step ahead
			current=current.next
			# move one step ahead 
			fast_traveler=fast_traveler.next	
		
		print(pos,"th Node From end of List is ",current)
			
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(60)
ll.add(70)
ll.add(80)
ll.display()
ll.NthFromEnd(3)
ll.NthFromEnd(2)
ll.NthFromEnd(10)

"""
	1) Find 3 rd Node From End
		Head								(Req)	
		10---->20---->30----->40----->50----->60------>70------>80------>NONE
                	Travel 

    2) Travel will move by N Steps
    	Head = 10
    	Travel = 30
    	Req = 60

    3) Move Head and Travel by one Step Until Travel Reach to End of List 

    4) Head Will Point to Nth Node from Node 	
"""