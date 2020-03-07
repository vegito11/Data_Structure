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
	
	# Construct a Tree by inserting given nodes 		
	def makeTree(self):
		self.insert(56)
		self.root.left=Node(13)
		self.root.right=Node(15)

		# 13
		self.root.left.left = Node(10)
		self.root.left.right = Node(3)

		# 15
		self.root.right.left = Node(9)
		self.root.right.right = Node(6)

	
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

	#### Find the Sum of Binary Tree . Maximum Height of Binary Tree
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

	# check if given node is Leaf Node : If no children then Leaf Node 	
	@staticmethod
	def _isLeaf(node):
		if node==None:return True
		if node.left==None and node.right==None:return True
		else:False		

	#### Find the Height of Binary Tree . Maximum Height of Binary Tree Complexity O(n)
	def isSumTree(self,root):
		"""
			if child Subtree are SUMTREE then there addition will be 2*childNode value
			Hence Root = 2*LeftChildValue + 2*rightChildValue
			Complexity O(n)
		"""
		# get status of is Leaf or Not 
		Leaf=self._isLeaf(root)
		leftSum=rightSum=0
		# we reach to end - node is empty Or Node is Leaf Node Ignore It
		if root==None or Leaf :
			return 1

		# breaking condition : If left child is Leaf Node return its value
		if self._isLeaf(root.left):
			leftSum = root.left.key

		# if Left Child is not Leaf Node 
		else:
			# this will sum of left subtree
			leftSum = 2*root.left.key 

		# breaking condition : If Right child is Leaf Node return its value
		if self._isLeaf(root.right):
			rightSum = root.right.key

		# if Right Child is not Leaf Node 
		else:
			# this will sum of right subtree
			rightSum = 2*root.right.key 
		
		status=int((leftSum+rightSum)==root.key)
		print(f'\n {root.key} = {leftSum}+{rightSum} {status}')
		if status==1:
			# also check if there child also sumTree
			status = self.isSumTree(root.left) and self.isSumTree(root.right)
			# print(status)
		return status	

	### Second Approach Complexity O(n^2)	: Uses Sum Method Above
	def isSumTreeApproach(self,root):
		"""
			Find left subtree height and right subtree height sum it and check it 
			with root Node 
		"""
		if root == None:
			return 1
		leftSum  = self.sumOfTree(root.left) 
		rightSum = self.sumOfTree(root.right)
		status = root.key == (leftSum+rightSum)	

		if status == True:
			status = self.isSumTreeApproach(root.left) and self.isSumTreeApproach(root.left)
			return status
		else: return False	

						

tree = Tree()
tree.makeTree()
tree.BfsTraversal()
status = tree.isSumTree(tree.root)
print("\n Given tree is Sumtree = ",status)

"""
					 56 
				13        15 
			10      3   9    6	
---------------------------------------------------
"""
"""
		   					 			  
"""