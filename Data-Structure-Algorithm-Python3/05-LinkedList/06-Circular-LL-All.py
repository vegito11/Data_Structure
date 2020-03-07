class Node:
	# constructor take data as argument and create new Node
	def __init__(self,data):
		self.data=data
		self.next=None

	def __str__(self):
		print(self.data,end="")
		return ""

from math import ceil

class CircularList(object):
	
	def __init__(self):
		self.head=None
		
	# get count of all nodes	
	def size(self):
		# if no element in list 
		if self.head==None : return 0
		# for traversing
		current = self.head 
		# initiallize length
		length=0
		while current.next!=self.head:
			# print("size: ",current)
			current=current.next
			length+=1 

		return length+1
###########==================================================############	
	# point new.next->Head . Then Head->new  
	def _addFirst(self,item):
		# create new node to add 
		new = Node(item)

		# for traversing
		current = self.head

		# travel to last node 
		while current.next!=self.head:
			print(current)
			current=current.next
		
		# point last node -> next to start node 
		current.next=new
		# new node next will point to old start 
		new.next=self.head
		# make new node new start
		self.head=new

		return				
	
	##===================================================##
	
	# add new node at middle of node
	def _addMiddle(self,item):
		new = Node(item)
		
		# 1) if only one item in list add at last 
		if self.head.next==self.head:
			print("Head Empty")
			# 1st node next will point to new node 
			self.head.next=new
			# 2nd node next to start node
			new.next=self.head

		# else size=2 add at 1 ; if 3 at 2 ; 4 at 2 ; 5 at 3
		else:
			result = self.getMid()	
			# if result is True 	
			if result[0]:
				# destruct tuple 
				_,prev,middle=result
				
				# point mid-1 position next to new node
				prev.next = new
				# new node next to middle node 
				new.next=middle
	
	##===================================================##
	
	# add new Node to Last
	def _addLast(self,item):
		new = Node(item)
		# for traversing
		current = self.head
		
		# Travel to Last Node. Then last->next = new
		while current.next!=self.head:
			current = current.next			
		
		# old last next to new node
		current.next = new
		# make new last next point to head
		new.next=self.head
		print("adding to last")
		return
	
	##===================================================##
	
	# add new node to given position	
	def _addAtPosition(self,item,position):	
		
		# if position of greater than List size+1 or negative
		if position > self.size()+1 or position < 0:
			print(" ^$%% --- Position Out of Bound $$%$% ---")

		# add item at first:	
		elif position == 1: self._addFirst(item)
		
		# add item at Last position
		elif position == self.size()+1 : self._addLast(item)

		# else add at positiom
		else:
			current = self.head
			new = Node(item)
			index=1
			# 10 20 
			# traverse to position-1 node suppose at 5 index 1,2,3,4			
			while index < position-1:
				print(index,position)		
				current=current.next
				index+=1
			
			tmp = current.next
			# new node at position
			current.next = new
			# point new.next->p+1 Node
			new.next = tmp

	##===================================================##		

	# add new node to head
	def add(self):
		# if head list is Empty make this node as Head Node 
		if not self.head:
			item = input("\n\t Enter Element : ")
			new = Node(item)

			self.head=new
			new.next=self.head
			return
		else:
			print("\n\t ******* Add At  ******* ")
			print("\t\t 1) Start \t 2) Middle \t 3) End  \t 4) Position \t 5) Exit")
			choice = eval(input("\t\t Element will be Added At Position : "))

			# add node at start of List
			if choice == 1 :
				item = input("\n\t Enter Element : ")
				self._addFirst(item)
				return
			# add node at Middle of List
			elif choice == 2:
				item = input("\n\t Enter Element : ")
				self._addMiddle(item)	
				return

			# add node at End of List
			elif choice == 3:
				item = input("\n\t Enter Element : ")
				self._addLast(item)	
				return

			# add node at Position of List
			elif choice == 4:
				item = input("\n\t Enter Element : ")
				position = eval(input("\t Enter Position : "))
				self._addAtPosition(item,position)
				# print("pos1")	
				return
			
			elif choice==5: return

			else:
				print(" $#$ Please Enter Valid Option #$#$")	

###########==================================================############

	# remove first item from List 
	def _removeFirst(self):
		
		# store node to be removed in tmp
		tmp=self.head
		
		# for traversing
		current=self.head
		
		# go to last node in list
		while current!=self.head:
			current=current.next

		# make second node as new Head Node
		self.head=tmp.next

		print(" Deleted ",tmp.data," from List ")
		del tmp		

		# make last->next point to new head Node	
		current.next=self.head	

	##===================================================##

	# ** (Two pointer for delete )remove last item from List 
	def _removeLast(self):
		# for traversing
		current=self.head

		# Traverse till Last Node
		while current.next!=self.head:
			# this will point to last-1 node 
			last=current
			current = current.next
		
		# Last node reference
		tmp=current
		# make new last node Next point to Start Node
		last.next=self.head
		print(" Deleted ",tmp.data," from List ")
		del tmp
	
	##===================================================##

	# remove middle item from List . If only one item take care by parent function
	def _removeMiddle(self):
		
		result = self.getMid()	

		# if result is True (at leat two element in List)
		if result[0]:
			# destruct tuple 
			_,prev,middle=result			
			# point mid-1 position mid+1 Node
			prev.next = middle.next
			print("Element ",middle," is removed from List !!!")
			middle=None
			# print("Element ",result[2]," is removed from List !!!")

	##===================================================##	

	# remove item at specified from List 
	def _removeAtPosition(self,position):
		
		# if position of greater than List size+1 or negative
		if position > self.size()+1 or position < 0:
			print(" ^$%% --- Position Out of Bound $$%$% ---")

		# remove first item from List:	
		elif position == 1: self._removeFirst()
		
		# remove last item from List:	
		elif position == self.size() : self._removeLast()

		# else remove Item from positiom
		else:
			current = self.head
			index=1
			# 10 20 
			# traverse to position-1 node suppose at 5 index 1,2,3,4			
			while index < position-1:
				# print(index)
				current=current.next
				index+=1
			# node to be deleted
			tmp = current.next
			# n-1 node will point to n+1 Node
			current.next = tmp.next
			# point new.next->p+1 Node
			print(" Deleted ",tmp.data," from List ")
			tmp=None
			del tmp

	##===================================================##		

	def remove(self):
		current = self.head
		
		# if list is empty
		if self.isEmpty():
			print(" !!! LinkedList is Empty !!! ")

		# if current item is only node in List 
		elif self.head.next==self.head:
			print(" Deleted ",current.data," from List ")
			del self.head
			self.head = None

		else:
			print("\n\t ******* Remove From  ******* ")
			print("\t\t 1) Start \t 2) Middle \t 3) End  \t 4) Position \t 5) Exit")
			choice = eval(input("\t\t Remove From which Location : "))

			# add node at start of List
			if choice == 1 :				
				self._removeFirst()
				return
			# add node at Middle of List
			elif choice == 2:				
				self._removeMiddle()	
				return

			# add node at End of List
			elif choice == 3:				
				self._removeLast()	
				return

			# add node at Position of List
			elif choice == 4:				
				position = eval(input("\t Enter Position : "))
				self._removeAtPosition(position)	
				return
			
			elif choice==5: return

			else:
				print(" $#$ Please Enter Valid Option #$#$")	

########==========================================############			
	
	def isEmpty(self):
		if self.head==None:
			return True
		return False			

########==========================================############			

	def display(self):

		# If no Item in Linked List
		if self.isEmpty():
			print(" !!! Linked List is Empty !!!")

		else:
			current=self.head
			while (current.next!=self.head):
				print(current,"=>",end=" ")
				current=current.next
			# print last node in Lisr
			print(current)	

########==========================================############			

	def getMid(self):
		
		if self.head==None or self.head.next==self.head:
			return False,

		fast=self.head
		slow=self.head
		prev=slow
		
		while True:
			prev=slow
			slow=slow.next
			fast=fast.next.next
			if fast==self.head or fast.next==self.head:
				break

		return True,prev,slow				
			
########==========================================############			

def mainMenu():
	
	while True:	
		print("\n ******* Menu ******* ")
		print("\n\t 1) Add \n\t 2) Remove \n\t 3) Display  \n\t 4) Size \n\t 5) Exit",end="\t\t")
		choice = eval(input("Enter the Option : "))
		
		# Add Item to Linked List
		if choice == 1:			
			ll.add()
		
		# Remove Item from Linked List
		elif choice == 2:
			ll.remove()
		
		# Traverse Linked List 	
		elif choice == 3:
			ll.display()
			
		# size			
		elif choice == 4:
			print("LinkedList  Size is : ",ll.size())				
		
		elif choice == 5 : break
		
		else:
			print(" %% $$ ## Enter valid Option !! !! !!")

ll = CircularList()

if __name__ == '__main__':
	mainMenu()

