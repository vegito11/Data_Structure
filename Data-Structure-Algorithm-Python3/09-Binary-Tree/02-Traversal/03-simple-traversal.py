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

	###### All Tree Tracversal #######
	## inorder traversal (it gives Sorted result) 
	# First Print Left , then Root and then Right 
	@classmethod
	def inorder(cls,subtreeHead):
		if subtreeHead==None:
			return
		cls.inorder(subtreeHead.left)
		print(subtreeHead.key,end="__")
		cls.inorder(subtreeHead.right)

		# first recursion result always be the head node 
		return subtreeHead

	## preorder traversal (Root always print First) 
	# First Print Root ; then Left and then Root 
	@classmethod
	def preorder(cls,subtreeHead):
		if subtreeHead==None:
			return
		print(subtreeHead.key,end="__")
		cls.preorder(subtreeHead.left)
		cls.preorder(subtreeHead.right)

		# first recursion result always be the head node 
		return subtreeHead

	## postorder traversal (Root always printed last) 
	# First Print Root ; then Left and then Root 
	@classmethod
	def postorder(cls,subtreeHead):
		if subtreeHead==None:
			return
		cls.postorder(subtreeHead.left)
		cls.postorder(subtreeHead.right)
		print(subtreeHead.key,end="__")

		# first recursion result always be the head node 
		return subtreeHead

tree = Tree()
tree.insert(27)
tree.insert(14)
tree.insert(10)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
tree.insert(9)
tree.insert(12)
tree.insert(29)
tree.insert(90)

print("Inorder Traversal: ",end="")
head = tree.inorder(tree.root)
print("\nHead of Node : ",head)
print("-"*50)

print("PreOrder Traversal: ",end="")
head = tree.preorder(tree.root)
print("\n","-"*50)

print("PostOrder Traversal: ",end="")
head = tree.postorder(tree.root)
print("\n","-"*50)
"""
					  27 
				14     |   35
		      10   19  | 31	42
		     9  12      29    90      
---------------------------------------------------
"""