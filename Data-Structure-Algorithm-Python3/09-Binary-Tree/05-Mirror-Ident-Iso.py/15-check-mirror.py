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
		self.insert(50)
		self.insert(23)
		self.insert(56)
		self.insert(21)
		self.insert(34)
		self.insert(53)
		self.insert(90)
	
	# Construct a Tree by inserting given nodes.
	def makeTreeMirror(self):
		self.insertReverse(50)
		self.insertReverse(23)
		self.insertReverse(56)
		self.insertReverse(21)
		self.insertReverse(34)
		self.insertReverse(53)
		self.insertReverse(90)
	
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

	# Two trees are Mirror of each other when left child==right child and vice versa
	@staticmethod
	def checkMirror(tree1,tree2):
		
		# CASE1 : If both tree node is None Hence Equal then Return True 
		if tree1==tree2: return True
		
		# CASE 2,3 : If one is Empty and other contain Data then no Match return False
		
		if tree1==None or tree2==None: return False  # we can also replace this with following line
		# if tree1==None and tree2!=None or tree1!=None and tree2==None: return False

		# CASE 4 : If two node data is not matched 
		if tree1.key!=tree2.key: return False
		
		# CASE 5 : If two node data is matched Check there children
		if tree1.key==tree2.key: 
		
			# CASE 5 : If Node1 LEFT == Node2 RIGHT and Node1 right == Node2 LEFT
			if Tree.checkMirror(tree1.left,tree2.right) and Tree.checkMirror(tree1.right,tree2.left):
				return True
			else: return False
			
tree1 = Tree()
tree1.makeTree()
tree1.BfsTraversal()
print()

tree2 = Tree()
tree2.makeTreeMirror()
tree2.BfsTraversal()
print()

result = Tree.checkMirror(tree1.root,tree2.root)
print(" Tree 1 is Mirror Of Tree2 is  = ",result)

tree1.insert(45)
tree1.insert(25)
tree1.BfsTraversal()
print()

result = Tree.checkMirror(tree1.root,tree2.root)
print(" Tree 1 is Mirror Of Tree2 is  = ",result)


"""
Two Trees are Isomorphic if One Tree left child is right child of another Tree
	1) 
		          50
		     23    |   56        
		  21   34  | 53   90
	2)	     
		          50
		     56    |   23        
		  34   21  | 90   53

	CASES : 
	1) If Two Are NONE then TRUE	  
	2) If Tree-1 is None and Tree-2 is Not EMPTY  return False
	3) If Tree-2 is None and Tree-1 is Not EMPTY  return False
	4) If Tree1.key!=Tree2.key then return False 
	5) If two node data is matched and 
		If Tree1.Left==Tree2.Right and Tree1.right==Tree2.left return TRUE
---------------------------------------------------
"""
"""
 
		   					 			  
"""