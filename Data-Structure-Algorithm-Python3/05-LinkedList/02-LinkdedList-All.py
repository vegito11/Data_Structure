class Node:
	# constructor take data as argument and create new Node
	def __init__(self,data):
		self.data=data
		self.next=None

	def __str__(self):
		print(self.data,end="")
		return ""

from math import ceil

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
	
	# point new.next->Head . Then Head->new  
	def _addFirst(self,item):
		new = Node(item)
		new.next=self.head
		self.head=new
		return				

	# add new node at middle of node
	def _addMiddle(self,item):
		new = Node(item)
		
		# 1) if only on item in list add at last 
		if self.head.next==None:
			print("Head Empty")
			self.head.next=new	

		# else size=2 add at 1 ; if 3 at 2 ; 4 at 2 ; 5 at 3
		else:
			position = ceil(self.size()/2) 
			
			# if only two element in the list
			if position == 1: 
				new.next=self.head.next
				self.head.next=new
				return

			print('position : ',position)
			self._addAtPosition(item,position) 	
	# add new Node to Last
	def _addLast(self,item):
		new = Node(item)
		
		current = self.head
		
		# Travel to Last Node. Then last->next = new
		while current.next!=None:
			current = current.next			
		
		current.next=new
		return

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
			while index != position:
				print(index)		
				current=current.next
				index+=1
			
			tmp = current.next
			# new node at position
			current.next = new
			# point new.next->p+1 Node
			new.next = tmp

	# add new node to head
	def add(self):
		# if head is null make this node as Head Node 
		if not self.head:
			item = input("\n\t Enter Element : ")
			new = Node(item)
			self.head=new
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
				return
			
			elif choice==5: return

			else:
				print(" $#$ Please Enter Valid Option #$#$")	

	#==============================================================
	# remove first item from List 
	def _removeFirst(self):
		tmp=self.head
		self.head=self.head.next
		print(" Deleted ",tmp.data," from List ")
		del tmp

	# ** (Two pointer for delete )remove last item from List 
	def _removeLast(self):
		current=self.head

		# Traverse till Last Node
		while current.next!=None:
			# this will point to last-1 node 
			last=current
			current = current.next
		
		# Last node reference
		tmp=current
		last.next=None
		print(" Deleted ",tmp.data," from List ")
		del tmp
					
	# remove middle item from List 
	def _removeMiddle(self):
		if self.size()==2: print(" !!! No Middle Element .... ")
		
		position = ceil(self.size()/2) 
		print('position : ',position)
		self._removeAtPosition(position)		

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
			while index != position:
				print(index)		
				current=current.next
				index+=1
			
			tmp = current.next
			current.next = tmp.next
			# point new.next->p+1 Node
			print(" Deleted ",tmp.data," from List ")
			del tmp

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
			print("\n\t ******* Remove From  ******* ")
			print("\t\t 1) Start \t 2) Middle \t 3) End  \t 4) Position \t 5) Exit")
			choice = eval(input("\t\t Remove Element from which position : "))

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
				print(current,"=>",end=" ")
				current=current.next
			
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

ll = LinkedList()

if __name__ == '__main__':
	mainMenu()

