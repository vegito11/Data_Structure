from Queue import Queue
class Node:
	def __init__(self,data):
		self.key=data
		self.left=None
		self.right=None

	def __str__(self):		
		return f'{self.key}'

class Tree:
	# it will initiallize root variable which point to ROOT of Tree
	def __init__(self):
		self.root = None

	# insert new node in tree left Small and right Greater	
	def insert(self,data):
		newNode=Node(data)		
		if self.root==None:
			self.root=newNode
			return

		current=self.root	
		while current!=None:
			if current.key>data:
				if current.left==None:
					current.left=newNode
					return
				else:
					current=current.left
			elif current.key<data:
				if current.right==None:
					current.right=newNode
					return
				else:
					current=current.right
			else:
				return		
	
	### insert new node in tree Right Small and Left Greater	
	def insertReverse(self,data):
		# create new node with given data
		newNode=Node(data)		
		if self.root==None:
			self.root=newNode
			return

		current=self.root	
		while current!=None:
			if current.key<data:
				if current.left==None:
					current.left=newNode
					return
				else:
					current=current.left
			elif current.key>data:
				if current.right==None:
					current.right=newNode
					return
				else:
					current=current.right
			else:
				return		
	
	# Construct a Tree by inserting given nodes.
	def makeTree(self):
		self.insert(90)
		self.insert(64)
		self.insert(96)
		self.insert(45)
		self.insert(78)
		self.insert(5)
		self.insert(56)
		self.insert(70)
		self.insert(89)
	
	# Construct a Tree by inserting given nodes.
	def makeTreeIso(self):
		self.insert(90)
		self.insertReverse(64)
		self.insertReverse(96)
		self.insertReverse(45)
		self.insertReverse(78)
		self.insertReverse(70)
		self.insertReverse(89)
		# print(self.root.right.right)
		self.root.right.right.left=Node(5)
		self.root.right.right.right=Node(56)

	## Breadth First Search / Level Order Traversal
	def BfsTraversal(self):
		# get the root address in variable 
		root = self.root

		# if tree doesn't contain any data 
		if root==None:
			return
		
		else:
			# create a new stack which will process last in first out 
			queue = Queue()
			# Apped root in Queue for first processing
			queue.enqueue(root)

			# repeat this until queue is not empty
			while  not queue.isEmpty():
				root=queue.dequeue()
				print(root,end="-")

				# if root contain left child append in Queue.It will processed in immediate iteration
				if root.left is not None:
					queue.enqueue(root.left)
				# if that root contain right child enqueue into Queue .
				if root.right is not None:
					queue.enqueue(root.right)

	@staticmethod
	def isIdentical(tree1,tree2):
		
		# CASE1 : If both tree node is None Hence Equal then Return True 
		if tree1==tree2: return True
		
		# CASE 2,3 : If one is Empty and other contain Data then no Match return False
		
		if tree1==None or tree2==None: return False  # we can also replace this with following line
		# if tree1==None and tree2!=None or tree1!=None and tree2==None: return False

		# CASE 4 : If two node data is not matched 
		if tree1.key!=tree2.key: return False
		
		# CASE 5 : If two node data is matched Check there children
		if tree1.key==tree2.key: 
		
			# CASE 5 : If Node1 LEFT == Node2 LEFT and Node1 right == Node2 RIGHT 
			if Tree.isIdentical(tree1.left,tree2.left) and Tree.isIdentical(tree1.right,tree2.right) :
					return True
			else: return False
			
tree1 = Tree()
tree1.makeTree()
tree1.BfsTraversal()
print()

tree2 = Tree()
tree2.makeTreeIso()
tree2.BfsTraversal()
print()

result = Tree.isIdentical(tree1.root,tree2.root)
print(" Tree 1 and Tree2 are Identical is  = ",result)

tree1.insert(45)
tree1.insert(25)
tree1.BfsTraversal()
print()

result = Tree.isIdentical(tree1.root,tree2.root)
print(" Tree 1 and Tree2 are Identical is  = ",result)

result = Tree.isIdentical(tree1.root,tree1.root)
print(" Tree 1 and Tree1 are Identical is  = ",result)


"""
    1) If three Level order Traversal is SAME
    2) There are also indentical If there ALL 3 Traversals are same 
	
	CASES : 
	1) If Two Are NONE then TRUE	  
	2) If Tree-1 is None and Tree-2 is Not EMPTY  return False
	3) If Tree-2 is None and Tree-1 is Not EMPTY  return False
	4) If Tree1.key!=Tree2.key then return False 
	5) If two node data is matched and 
		If Tree1.Left==Tree2.Left and Tree1.right==Tree2.right return TRUE
---------------------------------------------------
"""
