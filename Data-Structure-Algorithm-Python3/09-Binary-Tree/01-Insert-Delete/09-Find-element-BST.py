class Node:
	# constructor take name and age as argument and create new Node
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
	# insert new node in tree	
	def insert(self,data):
		
		# create new node with given data
		newNode=Node(data)
		
		# if root is empty no data in TREE new Node will be Root of Tree
		if self.root==None:
			self.root=newNode
			return

		current=self.root	
		while current!=None:

			# if new node data is smaller than this node go to LEFT of Tree
			if current.key>data:
				
				# if left subtree is empty then make this node a left subtree
				if current.left==None:
					current.left=newNode
					return
				# if left subtree is not empty traverse to left to search for this node position	
				else:
					current=current.left
			
			# if new node data is greater than this subtree data go to RIGHT of tree
			elif current.key<data:
				
				# if right subtree is empty then make this node a right subtree
				if current.right==None:
					current.right=newNode
					return
				# if right subtree is not empty traverse to right to search for this node position	
				else:
					current=current.right
			# if this subtree data is same as new Data then do not insert
			else:
				return		

	def makeTree(self):
		self.insert(27)
		self.insert(14)
		self.insert(10)
		self.insert(35)
		self.insert(10)
		self.insert(19)
		self.insert(31)
		self.insert(42)
		self.insert(9)
		self.insert(12)
		self.insert(29)
		self.insert(90)

	## Breadth First Search / Level Order Traversal
	
	# print and return True or False depending upon element present in given Tree
	@classmethod	
	def find(cls,element,root):
		# if we did not found given element in tree
		if root==None: 
			print(f' !!! {element} Not in Tree')
			return False

		if root.key==element:
			print(f'We found {element} in Tree')
			return True	
		# if given element value is less than Current Root Then search in Left side of tree
		elif root.key>element:
			# go to left side of tree for Smaller elements
			cls.find(element,root.left)
		# Element is Greater than Root	
		elif root.key<element:
			# go to right side of tree for Greater elements
			cls.find(element,root.right)
	
	# find Minimum valued Node in tree
	@classmethod	
	def findMin(cls,root):
		# if given tree is Empty
		if root==None:
			print(" Given Tree is Empty")
		# breaking condition current Node is Left most node in Tree
		if root.left==None:
			print(f'{root} is Minimum Valued node in Tree .. ')
			return root
		root = cls.findMin(root.left)	
		return root

	# find Maximum valued Node in tree
	@classmethod	
	def findMax(cls,root):
		# if given tree is Empty
		if root==None:
			print(" Given Tree is Empty")
		# breaking condition current Node is Left most node in Tree
		if root.right==None:
			print(f'{root} is Maximum Valued node in Tree .. ')
			return root
		root = cls.findMax(root.right)
		return root


						

tree = Tree()
tree.makeTree()
tree.find(20,tree.root)
tree.find(90,tree.root)
print("-"*50)
tree.findMin(tree.root)
print("-"*50)
tree.findMax(tree.root)

"""
					     27 
				  14     |      35
		      10     19  |   31	   42
		     9  12       | 29        90      

	BFS:  27-14-35-10-19-31-42-9-12-29-90-
---------------------------------------------------
"""
 