class Node:
	# constructor take name and age as argument and create new Node
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.next=None

	def __str__(self):
		# print(" Name : ",self.name)
		# print(" age  : ",self.age)
		print(f' Name : {self.name} -- Age : {self.age} ')
		return ""

n = Node("omkar",10)
# print(n)

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
		
		new = Node(data['name'],data['age'])
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
			print(" Deleted ",current.name," from List ")
			del self.head
			self.head = None

		else:
			self.head=current.next
			print(" Deleted ",current.name," from List ")
			del current
			
			

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
			

ll = LinkedList()

ll.add({'name':'Omkar','age':20})
ll.add({'name':'Ethun','age':40})
ll.add({'name':'Vegito','age':70})

ll.display()

print(ll.size())
ll.remove()
ll.remove()
ll.remove()
ll.remove()
print(ll.size())

ll.add({'name':'Ethun','age':40})
ll.add({'name':'Vegito','age':70})

ll.display()
