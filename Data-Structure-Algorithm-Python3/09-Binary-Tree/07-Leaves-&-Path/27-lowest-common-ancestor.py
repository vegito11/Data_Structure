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
		self.insert(15)
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

	@staticmethod
	def isLeaf(node):
		if node==None: return False
		if node.left==None and node.right==None: return True
		else: return False
	
	#### print all the Node having K Leaf Nodes
	@classmethod
	def getAncestors(cls,root,node1,node2):

		# if we reach to end node of subtree  Break Condition
		if root==None: return None

		# breaking condtion : If current node is one of the Node to find then return this Node
		if root.key==node1 or root.key==node2:
			return root

		inLeft  = cls.getAncestors(root.left,node1,node2)
		inRight = cls.getAncestors(root.right,node1,node2)

		# if both the subtree return the Nodes then this Node is LCA
		if inLeft!=None and inRight!=None:
			return root

		return  inRight if (inLeft==None)  else inLeft

tree = Tree()
tree.makeTree()
node1=79
node2=87
print(" Lowest common Ancestor of Node %d and Node %d is : "%(node1,node2),tree.getAncestors(tree.root,node1,node2))
print(" Lowest common Ancestor of Node %d and Node %d is : "%(14,60),tree.getAncestors(tree.root,14,60)) # 14
print(" Lowest common Ancestor of Node %d and Node %d is : "%(85,36),tree.getAncestors(tree.root,85,36)) # 50
print(" Lowest common Ancestor of Node %d and Node %d is : "%(45,5),tree.getAncestors(tree.root,45,5)) # 16

print("  !!!! Even if one of the Node is not exist !!! ")

print(" Lowest common Ancestor of Node %d and Node %d is : "%(145,87),tree.getAncestors(tree.root,145,87)) # 87
print(" Lowest common Ancestor of Node %d and Node %d is : "%(145,5),tree.getAncestors(tree.root,145,5))  # 5
print(" Lowest common Ancestor of Node %d and Node %d is : "%(145,905),tree.getAncestors(tree.root,145,905)) # None
print()
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
	Get Ancestor of Given Node 

	1) It is first common node in ancestor between two nodes 
	2) Search N1 and N2 in Children
	2) Search in left and right child 
		one child : Node-1   second child : NONE         Return NODE-1
		one child : NONE     second child : NODE-2       Return NODE-2
		one child : NONE     second child : NONE         Return NONE
		one child : Node-1   second child : Node-2       -- This LCA

	3) We are using InOrder Traversal here (Process root after we get result from left )
	4) Use of INORDER is that When we get result from left subtree then we process root and then 
	   go to right subtree we get result from that and then return this result to parent (root)


"""