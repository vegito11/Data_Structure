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
	
	# is List is Empty ? 		
	def isEmpty(self):
		if self.head==None:
			return True
		return False			

	# display list
	def display(self):

		if self.head==None: return None
		else:
			current=self.head
			while (current!=None):
				print(current,"=>",end=" ")
				current=current.next
			print("NULL")


	# 10=>20=>30=>40=>50=>60=>70
	# 50=>60=>70=>10=>20=>30=>40=>None
	def RotateAroundNode(self,node=40):
		
		# store first node address in this variable
		current=self.head

		# if only one node in List 
		if current==None or current.next==None:
			return current

		# travel till last node 
		while current!=None:

			# if current  data is rotating point
			if current.data == node:
				break
			# if we have reached to last Node and still not found a node 	
			if current.next==None: 
				return	
			current=current.next	

		# Store Next Node of Rotating Node 
		secondListHead=current.next

		# make First List , LastNode.next None to end this List
		current.next=None
		
		# start from second node start(60)
		travel_to_last = secondListHead

		# travel till we reach to LastNode
		while travel_to_last.next!=None:
			# move one step ahead
			travel_to_last=travel_to_last.next

		# secondList End will point to First List Head 
		travel_to_last.next=self.head	

		# make secondList Head new Head of main List 
		self.head=secondListHead

				
ll = LinkedList()
ll.add(10)
ll.add(20)

ll.display()
ll.RotateAroundNode(10)
ll.display()

ll.add(30)
ll.add(40)
ll.add(60)
ll.add(70)
ll.add(80)

ll.display()
ll.RotateAroundNode(30)
ll.display()


"""
	1) Rotate around Node 50 
		
		10---->20---->30----->40----->50----->60------>70------>80------>NONE
		
		60------>70------>80----->10---->20---->30----->40----->50------>NONE

    2) Travel Till node 50 
	
	3) Make its next NONE
    
    4) new head of Second List from 60 to 80 .

    5) make end node.next of Second List point to Head of First Node 

    6) Make 80 (start of second list ) as Head of new LL 

"""