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

	@staticmethod	
	def reverseList(head):
		
		# if last it will return last node 
		if head==None or head.next==None:
			return head
		
		first=head
		# to pass for next iteration
		second = head.next

		newStart = LinkedList.reverseList(second)	
		
		# reverse Link
		first.next.next = first
		first.next=None

		return newStart	

	@staticmethod
	def display(head):

		if head==None: return None
		else:
			current=head
			while (current!=None):
				print(current,"=>",end=" ")
				current=current.next
			print("NULL")

	# 10=>20=>30=>40=>30=>20=>10
	# check if given Linked List is palindrome
	def checkPalindrome(self):
		
		# if give list contain less than two node 
		if self.head==None or self.head.next==None :
			return False

		slow = self.head
		fast = self.head
		# if we have written fast.next first it will be problem 🤨
		beforeMiddle=None
		while fast!=None and fast.next!=None:
			beforeMiddle=slow
			# move one step ahead ! at the end we will reach to middle
			slow=slow.next
			# move two step ahead
			fast=fast.next.next
		
		######## SLOW Will be middle of List  and start of next List (Even)#####
		# new list end
		beforeMiddle.next=None
		
		# odd length Linked List 
		if fast!=None:
			# reverse next half (ignore middle element which is common)
			newHead = LinkedList.reverseList(slow.next)
		else:	
			# reverse next half 
			newHead = LinkedList.reverseList(slow)				
		

		LinkedList.display(self.head)
		LinkedList.display(newHead)
		
		# start comparing two list
		ListOneHead=self.head
		ListTwoHead=newHead
		while ListOneHead:
			if ListOneHead.data!=ListTwoHead.data:
				return False
			ListOneHead=ListOneHead.next
			ListTwoHead=ListTwoHead.next

		return True	



			
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(30)
ll.add(20)	
ll.add(10)	
ll.display(ll.head)
Ans = ll.checkPalindrome()

if Ans==True:
	print(" ..... Given List is Palindrome ..... ")
else:
	print(" !!!! Given List is NOT Palindrome !!!! ")


"""
	1) a=>b=>c=>d=>d=>c=>b=>=>a
	2) a=>b=>c=>d=>e=>d=>c=>b=>=>a
	
	STEPS : 

	1) Go to middle of List 
	2) mark Prev Node of Middle next == None  . First list will be made 
	3) second List will start from Slow (if Even List) . from Slow.next if List is Odd
	4) reverse second list

"""