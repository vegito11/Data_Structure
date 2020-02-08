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
		self.insert(35)
		self.insert(45)
		self.insert(75)
		self.insert(15)
		self.insert(82)
		self.insert(81)
		self.insert(85)
		self.insert(79)
		self.insert(87)
		self.insert(5)
		self.insert(32)
		self.insert(36)
		self.insert(37)

	#### Find the Height of Binary Tree . Maximum Height of Binary Tree
	def heightOfTree(self,root):
		"""
			Height = 1+Number of **Edges on the longest path from root to leaf

			We calculate left and right subtree height and then choose whiche child (left or right) 
			height is greater then choose it and add 1 to it to get parent height 

			First left and right child height is calculated then it will return to its parent 
		"""
		# we reach to end
		if root==None:
			return 0

		leftSubtreeHeight  = self.heightOfTree(root.left)
		rightSubtreeHeight = self.heightOfTree(root.right)

		# height = 1+(leftSubtreeHeight if leftSubtreeHeight > rightSubtreeHeight else rightSubtreeHeight)
		
		if leftSubtreeHeight > rightSubtreeHeight : 
			height= 1+leftSubtreeHeight
		elif rightSubtreeHeight >= leftSubtreeHeight:
			height= 1+rightSubtreeHeight	
		
		print("%4d Tree : %2d "%(root.key,height),end=" | \t")
		""" Just for Formatting purpose Ignore this  """
		global cnt 
		cnt+=1
		if cnt%6==0:print()
		""" END"""	
		return height

						

tree = Tree()
tree.makeTree()
Height = tree.heightOfTree(tree.root)
print("\nHeight Of Tree is  = ",Height)

"""
					  	         50 
				        16   	    |       90
		        14         40	    |    78	    100
		     10   15     35     45  | 75     82  	
			5		   32   36	    |	   81    85
							  37    |	 79        87	

LMR:  5-10-14-16-32-34-35-37-40-45-50-75-78-79-81-82-85-87-90-100-
---------------------------------------------------
"""
"""
	When we pass 50 it will calcuate its child height 
	max of height(16) 				  	  |			 height(90)
		max of height(14)  height(40) 	  | max of height(78) , height(100)
		 m ht(10),ht(15), m ht(35),ht(45) |  m ht(75),ht(82), ||
		   ht(5)+0 : 0+0, ht(32)+ht(36):0 |   0 , ht(81)+ht(85) ||  
		   	 	   : 0+0, 0 # +ht(37)+0   |   0 , ht(79)+0 : 0+ht(87) ||  
		   					 			  
"""