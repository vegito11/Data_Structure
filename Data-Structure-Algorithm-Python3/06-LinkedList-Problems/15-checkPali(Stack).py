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

	# 10=>20=>30=>40=>30=>20=>10
	# check if given Linked List is palindrome
	def checkPalindrome(self):
		# create new stack/List as Stack
		Stack = []
		
		# if give list contain less than two node 
		if self.head==None or self.head.next==None :
			return False

		# for pointing to Middle Element	
		slow = self.head
		# for traversing list
		fast = self.head
		
		# if we have written fast.next first it will be problem 🤨
		while fast!=None and fast.next!=None:
			# Push element in stack 
			Stack.append(slow)
			
			# move one step ahead ! at the end we will reach to middle
			slow=slow.next
			# move two step ahead
			fast=fast.next.next
		
		# if length if List is EVEN 	
		SecondStart = slow

		# if legth of list is ODD Start Second List from Middle+1 Element
		if fast!=None:
			SecondStart = slow.next
		
		# compare till Stack is not Empty		
		while Stack!=[]:
			# Pop Element from STACK and compare it with Second List
			Top = Stack.pop()

			# if not matched not a palindrome
			if Top.data != SecondStart.data:
				return False
			
			# move one step ahead in Second List 			
			SecondStart=SecondStart.next	

		return True	



			
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
# ll.add(40)
ll.add(30)
ll.add(20)	
ll.add(10)	
ll.display()
Ans = ll.checkPalindrome()

if Ans==True:
	print(" ..... Given List is Palindrome ..... ")
else:
	print(" !!!! Given List is NOT Palindrome !!!! ")


"""
	1) a=>b=>c=>d=>d=>c=>b=>=>a
	2) a=>b=>c=>d=>e=>d=>c=>b=>a
	
	STEPS : 

	1) Go to middle of List . by pushing data in stack
	2) second List will start from Slow (if Even List) . from Slow.next if List is Odd
	4) Pop one by one from List and compare It 

"""