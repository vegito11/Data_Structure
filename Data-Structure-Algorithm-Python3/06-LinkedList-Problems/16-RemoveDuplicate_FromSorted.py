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

	# 10 => 10 => 30 => 30 => 60 => 70 => 90 => 90 => NULL
	# remove duplicate from sorted List
	def removeDuplicates(self):
		current=self.head

		# if list contain only one element
		if current==None or current.next==None:
			return current

		# travel till we reach to end of list 
		while current and current.next!=None:
			
			# if two nodes data match each other which are back and forth
			if current.data==current.next.data:
				
				# skip the duplicate node by pointing backNode.next to forthNode.next
				current.next = current.next.next  
			
			# current will store new Non Duplicate Node like (30,60,70,90) when not matched
			else:	
				# move current Node to next Node if two nodes are not matching
				current=current.next
			
ll = LinkedList()
ll.add(10)
ll.add(10)
ll.add(30)
ll.add(30)
ll.add(30)
ll.add(60)	
ll.add(70)	
ll.add(90)	
ll.add(90)	
ll.add(90)	
ll.display()
ll.removeDuplicates()
ll.display()


"""
	1) Rotate around Node 50 
		
		10---->10---->30--->30--->30--->60--->70--->90---->-->90--->NONE
		
		10------>30------>60----->70---->90---->NONE

"""