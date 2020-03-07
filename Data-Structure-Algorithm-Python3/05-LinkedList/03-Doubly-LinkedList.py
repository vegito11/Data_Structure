class Node:
	# constructor take name and age as argument and create new Node
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.next=None
		self.prev=None

	def __str__(self):
		return f' Name : {self.name} -- Age : {self.age} '
		return ""

n = Node("omkar",10)
# print(n)

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
	def add(self,data):
		
		new = Node(data['name'],data['age'])
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
			print(" Deleted ",current.name," from List ")
			del self.head
			self.head = None			

		else:
			# store node to be deleted in temp
			tmp = current
			# make 2nd node first Node
			self.head=current.next
			self.head.prev=None
			print(" Deleted ",tmp.name," from List ")
			del tmp
						

	def isEmpty(self):
		if self.head==None:
			return True
		return False			

	def display(self):

		# If no Item in Linked List
		if self.isEmpty():
			print(" !!! Linked List is Empty !!!")

		else:
			current=self.head
			while (current!=None):
				print(current)
				current=current.next
			

dll = DoublyLinkedList()

dll.add({'name':'Omkar','age':20})
dll.add({'name':'Ethun','age':40})
dll.add({'name':'Vegito','age':70})

dll.display()

print(dll.size())
dll.remove()
dll.remove()
dll.remove()
dll.remove()
print(dll.size())

dll.add({'name':'Ethun','age':40})
dll.add({'name':'Vegito','age':70})

dll.display()
