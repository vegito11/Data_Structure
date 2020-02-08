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

	## Vertical Order Traversal . Print Node lines from Left to Right 
	def verticalOrder(self):

		# if tree is empty exit
		if self.root==None: return
		

		# initiallize Queue which will helpful for level order Traversal
		node_queue=Queue()

		# add the root in the Queue
		node_queue.enqueue(self.root)
		# this will add None in Queue so will get to know that this is this level end 
		node_queue.enqueue(None)
		level=1
		# Repeat until queue is not Empty 	
		while not node_queue.isEmpty():
			
			node = node_queue.dequeue()	

			# if this is None means new LEVEL Diagonal is starting Like 1,2,3,4 (see in Image) 
			if node==None:
				
				# add this to end of Queue . Because now we are at new Level so Mark end of old level
				node_queue.enqueue(None)

				# get the new node (from start )
				node = node_queue.dequeue()

				# if back to back None Means Queue is Empty Exit the While Loop
				if node==None:
					break
				
				print(f"\n-----------{level}------------")
				level+=1

			# while node is not None move to right of node (we get Same Level Element that is Diagonal)
			while node!=None:					
				print(node,end=" ")
				# if this node Left child is exit
				if node.left:
					# Enqueue it in the Queue 
					node_queue.enqueue(node.left)

				# move to left of current node
				node=node.right

			# when moved to rightmost part we get new node from start of queue and now if it is None means 
			# this menas we have comepleted this level If not None we will traverse same level 	

tree = Tree()
tree.makeTree()

print(" -------------------- Vertical Order Traversal Traversal ------------------- ")
tree.verticalOrder()
print("\n","-"*75)

"""
					     27 
				  14     |      35
		      10     19  |   31	   42
		     9  12       | 29        90      

	
---------------------------------------------------
"""
"""
	* Print All Diagonal Elements of a Binary Tree 

	Rules to Mark d
	1) d = d + 1 only for left child 
	2) for every right child 
		d = d of parent ( d remains same for right child ) 
	
	Algorithm :

	1) Insert Root and then None 
	2) Move toward right of that Root . If that right child have left child Enqueue it into Queue 
	3) Because we require this for next sequence of (2,3,..,..) diagonal Level Element 
	
	4) Once we reach end of right of that tree 

	5) Enqueue None to the Queue To mark End of Diagonal Element Level .

"""