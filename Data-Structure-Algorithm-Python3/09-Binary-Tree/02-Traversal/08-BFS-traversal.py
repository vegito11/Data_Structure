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


						

tree = Tree()
tree.makeTree()

print("Depth First Traversal   : ",end="")
tree.BfsTraversal()
print("\n","-"*50)

"""
					     27 
				  14     |      35
		      10     19  |   31	   42
		     9  12       | 29        90      

	BFS:  27-14-35-10-19-31-42-9-12-29-90-
---------------------------------------------------
"""
 