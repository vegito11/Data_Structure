class Node:
	# constructor take name and age as argument and create new Node
	def __init__(self,data):
		self.key=data
		self.left=None
		self.right=None

	def __str__(self):		
		return f'{self.key}'
cnt=0		
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
		self.insert(15)
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
		self.insert(36)
		self.insert(37)

	# inorder traversal of Tree 	
	def inorder(self,root):
		if root==None:return
		self.inorder(root.left)
		print(root,end="--")	
		self.inorder(root.right)

	#### Find the Sum of Binary Tree . Maximum Sum of Binary Tree
	def sumOfTree(self,root):
		"""
			Sum = current Node data + left subtree sum + right subtree sum
			When reach to 
		"""
		# we reach to end 
		if root==None:
			return 0
		else:	
			sum = root.key + self.sumOfTree(root.left) + self.sumOfTree(root.right)				
		return sum

						

tree = Tree()
tree.makeTree()
tree.inorder(tree.root)
print()
Sum = tree.sumOfTree(tree.root)
print("\nSum Of Tree is  = ",Sum)

tree1 = Tree()
tree1.insert(25)
tree1.insert(34)
tree1.insert(16)
tree1.insert(30)
tree1.insert(35)
tree1.insert(4)
tree1.inorder(tree1.root)
print()
Sum = tree1.sumOfTree(tree1.root)
print("\nSum Of Tree is  = ",Sum)

"""
					  	         50 
				        16   	    |        90
		        14         40	    |    78	      100
		     10   15     35     45  | 75     82  	
			5		   32   36	    |	   81    85
							  37    |	 79        87	

LMR:  5-10-14-16-32-34-35-37-40-45-50-75-78-79-81-82-85-87-90-100-
---------------------------------------------------
"""
"""
             25 
         16      34
       4       30   35 		   					 			  
"""
