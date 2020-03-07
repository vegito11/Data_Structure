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
	
	# Construct a Tree by inserting given nodes 		
	def makeTree(self):
		self.insert(50)
		self.insert(16)
		self.insert(90)
		self.insert(14)
		self.insert(40)
		self.insert(78)
		self.insert(100)
		self.insert(10)
		self.insert(35)
		self.insert(45)
		self.insert(75)
		self.insert(82)
		self.insert(81)
		self.insert(85)
		self.insert(79)
		self.insert(87)
		self.insert(5)
		self.insert(32)
		self.insert(34)
		self.insert(37)

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

	# Previous Small element	
	## return Inorder Predecessor of Given element  (Left Root Right)
	def InOrderPred(self,key):
		"""
		CASE 1 : If this Node has Left child find the minimum valued node Than this node 
		         it will be predecessor
		CASE 2 : If this Node does not have left child . Find the Node who has **taken last right Turn 
		CASE 3 : If Node do not have any predeccor . FIRST Inorder Node
		"""
		lastRight=None
		current = self.root
		# print(current)
		while current!=None:
			# if key is less than current node move left 
			if current.key>key:
				current=current.left

			# if key is less than current node move right 
			if current.key<key:
				lastRight=current
				current=current.right
			# if we find the 	required element node 
			if current.key==key:
				# print(lastRight)
				
				# CASE 1 : if this node has left subtree
				if current.left:
					
					# traverse left subtree for max element
					current=current.left

					# find max in left subtree 
					while current.right!=None:
						# search for greater element
						current=current.right
					print(" Predecessor of Node ",key," is : ",current)	
						
				# CASE 2 : if this node do not have left child and lastRight
				elif current.left==None and not lastRight:
					print(" !!! Node ",key," do not have Predecessor !!!! ")

				# CASE 3 : if this node do not have left child and have a lastRight
				elif current.left==None and  lastRight:
					print(" Predecessor of Node >> ",key," is : ",lastRight)	
					
				return
						

tree = Tree()
tree.makeTree()
tree.inorder(tree.root)
print()
tree.InOrderPred(40)
tree.InOrderPred(32)
tree.InOrderPred(78)
tree.InOrderPred(5)

"""
					  	         50 
				      16   	      |   	   90
		        14        40	  |    78	    100
		     10   15   35     45  | 75     82  	
			5		 32   36	  |		 81    85
							37    |	   79        87	

LMR:  5-10-14-16-32-34-35-37-40-45-50-75-78-79-81-82-85-87-90-100-
---------------------------------------------------
"""
 