class Node:
	# constructor take name and age as argument and create new Node
	def __init__(self,age):
		self.age=age
		self.next=None
		self.prev=None

	def __str__(self):
		return str(self.age)

class DoublyLinkedList(object):
	
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
	def add(self,age):
		
		new = Node(age)
		# if head is null make this node as Head Node 
		if not self.head:
			self.head=new
		
		# Insert this node as first Node
		else:
			self.head.prev=new
			new.next= self.head 
			self.head=new
	
	# remove node from head
	def remove(self):
		current = self.head
		
		# if list is empty
		if self.isEmpty():
			print(" !!! DoublyLinkedList is Empty !!! ")

		# if current item is only node in List 
		elif self.head.next==None:
			print(" Deleted ",current.age," from List ")
			del self.head
			self.head = None			

		else:
			# store node to be deleted in temp
			tmp = current
			# make 2nd node first Node
			self.head=current.next
			self.head.prev=None
			print(" Deleted ",tmp.age," from List ")
			del tmp
						
	def isEmpty(self):
		if self.head==None:
			return True
		return False			

	def display(self):

		# If no Item in Linked List
		if self.isEmpty():
			print(" !!! Linked List is Empty !!!")
			return 

		else:
			current=self.head
			while (current!=None):
				print(current.age,end="=>")
				current=current.next
		print("None")
	# reverse Doubly Linked List 
	def reverseDLL(self):
		# save first node address in this variable
		current = self.head
		
		# if list contain only one element
		if current==None or current.next==None:
			return current

		prev = None 

		# when we reach to last_node.next 
		while current!=None:
			# store this for next iteration
			next = current.next
			
			# reverse a link 			
			  # next will point to previous Backward Node 
			current.next=prev
			  # prev will point to previous Forward Node 
			current.prev=next
			# print(current)
			# for next iteration this node will be  required 
			prev=current
			# move to next next iteration
			current=next
		# print(prev)
		self.head=prev

dll = DoublyLinkedList()

dll.add(20)
dll.add(40)
dll.add(70)
dll.add(50)
print("-"*40)
dll.display()
dll.reverseDLL()
dll.display()
print("-"*40)
dll.remove()
dll.add(80)
dll.display()
print("-"*40)
"""
			  n    n    n    n    n
 	START==10==>20==>30==>40==>50==>None
              <-p   <-p  <-p   <-p    
		 
		  n	   n    n    n    n 
	NONE<==10<==20<==30<==40<==50==START
            p->  p-> p->  p->   
"""