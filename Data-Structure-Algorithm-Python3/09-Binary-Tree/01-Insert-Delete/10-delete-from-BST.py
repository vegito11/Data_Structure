from Queue import Queue
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
	
	# Construct a Tree by inserting given nodes 		
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
		self.insert(38)
		self.insert(40)
		self.insert(41)

	# delete element if present in tree with given root , parent paramater used for to adjust its value
	# for deleted node new replacements
	@classmethod	
	def delete(cls,element,root,parent=None):
		# if we did not found given element in tree
		if root==None: 
			print(f'\n !!! {element} Not in Tree')
			return False

		# if given element value is less than Current Root Then search in Left side of tree
		elif root.key>element:
			# go to left side of tree for Smaller elements
			cls.delete(element,root.left,parent=root)

		# Element is Greater than Root	
		elif root.key<element:
			# go to right side of tree for Greater elements
			cls.delete(element,root.right,parent=root)
		
		# ** When parent is None add your code for this CASE *** 
 		#### When we find element Delete this element
		if root.key==element:

			# CASE : 1) if this Node do not have any child 
			if root.left==None and root.right==None:
				print(root,",,",parent)

				# if node to be deleted is RIGHT CHILD of parent
				if parent.right==root:
					# make deleted node parent right point to None 
					parent.right=None
				
				# if node to be deleted is LEFT CHILD of parent
				else:	
					# make deleted node parent left  Point to None
					parent.left=None
				root=None

			# CASE 2) if this node have only left child (right node is None)
			elif root.right==None:
				print(root,",,",parent)

				# if node to be deleted is RIGHT CHILD of parent
				if parent.right==root:
					# make deleted node parent right point to Left subtree of deleted child 
					parent.right=root.left
				
				# if node to be deleted is LEFT CHILD of parent
				else:	
					# make deleted node parent left point to Left subtree of deleted child 
					parent.left=root.left
				root=None

			# CASE 2) if this node have only right child (left node is None)
			elif root.left==None:
				print(root,",,",parent)

				# if node to be deleted is RIGHT CHILD of parent
				if parent.right==root:
					parent.right=root.right
				
				# if node to be deleted is LEFT CHILD of parent
				else:	
					parent.left=root.right
				root=None
			
			# CASE 3) if this node has BOTH left and right childern
			else:
				# find MIN element from RIGHT subtree or 
				# MAX element from LEFT subtree and make it as new Root
				##### Get new max node from left subtree of given root
				LeftMaxElem,parent = cls.findMax(root.left)
				root.key=LeftMaxElem.key
				cls.delete(LeftMaxElem.key,root.left,parent)
				
		return True	
	
	# find Maximum valued Node in tree from Given Root Position,and also its parent
	@classmethod	
	def findMax(cls,root):
		current_node = root
		parent=None
		while current_node.right: 
			parent=current_node
			current_node = current_node.right
		return current_node,parent


						

tree = Tree()
tree.makeTree()

tree.BfsTraversal()
tree.delete(20,tree.root)
print("-"*50)

tree.delete(27,tree.root)
tree.BfsTraversal()
print("\n","-"*50)

"""
					     27 
				  14     |      35
		      10     19  |   31	    42
		     9  12       | 29     38    90      
									40
								      41	
	BFS:  27-14-35-10-19-31-42-9-12-29-90-
---------------------------------------------------
"""
 