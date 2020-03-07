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

	def swapNodes(self,data1,data2):
		
		# if List is empty or only one Node in List
		if self.head==None or self.head.next==None:
			return self.head
		
		# if both the items are same . no change
		elif data1==data2:
			return self.head	
		
		# initialize two variable which will point to previous of this two nodes
		previous=prevNode1=prevNode2=None
		item1_Node=item2_Node=None
		
		# for traversing list initialize to start Node
		current=self.head
		
		###==== Find Previous Node of Items and Items Node Address ###
		# run till current is not None 
		while current:
			
			# if this node is item1 Node  
			if current.data==data1:
				
				# store address of Item1 Nodes previous Node in this variable
				prevNode1=previous
				
				# this node contain Item1/data1 Node information
				item1_Node=current
			
			# if this node is item2 Node  
			elif current.data==data2:
				
				# store address of Item2 Nodes previous Node in this variable
				prevNode2=previous

				# this node contain Item2/data2 Node information
				item2_Node=current

			# store current node address which will be useful in next step	
			previous=current
			# move pointer by one step	
			current=current.next

		# print(item1_Node)
		# print(item2_Node)
		### If ane of the items not present in list 
		if not item1_Node or not item2_Node:
			print(" Item/s are not present in List !!!! ")
			return self.head

		#### If Any of node previous is None then there will be problem ###
		tmp = item2_Node.next
		# modify the next pointer of each Nodes
		item2_Node.next=item1_Node.next 
		item1_Node.next=tmp

		
		# if first item Node is Head/Start Node. It will not have any previous.
		if self.head==item1_Node:
			# new Start Node head will be Second Item Node 
			self.head=item2_Node
			# second_Item_node_next will point to First item Node 
			prevNode2.next=item1_Node
		
		#### elif not if bcz item2_Node will become Start Node after swapping
		# if second item Node is Head/Start Node.It will not have any previous.
		elif self.head==item2_Node:
			# new Start Node head will be First Item Node 
			self.head=item1_Node
			# first_Item_node_next will point to Second item Node 
			prevNode1.next=item2_Node

		# if both are internal node , hence both will hava previous Node 
		else:
			# First_Node_Previou_next Will Point to Second node 
			prevNode1.next=item2_Node
			# Second_Node_Previou_next Will Point to First node 
			prevNode2.next=item1_Node
			
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.add(60)	
ll.display()

ll.swapNodes(10,50)
ll.display()

"""
	10=>20=>30=>40=>None

	1) if one of them is Head Node 
	2) one of them last node 



"""