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
		
		# This is Map which will store the Horizontal Distance of each Node 
		hd_of_nodes={}   # {Node1:-1,Node10:3}
		
		# this is map which will map KEY (Hd) : [list of same hd Node ] 
		hd_group={} # 0{-3:[9,],0:[27,19,31]}

		# start from the root of the tree
		start = self.root

		# store root node Horizontal Distance first
		hd_of_nodes[start]=0

		# initiallize Queue which will helpful for level order Traversal
		level_traversal_queue=Queue()

		# add the root in the Queue
		level_traversal_queue.enqueue(start)
		
		while not level_traversal_queue.isEmpty():
			# get the last enqueue node to Check its child 

			parent = level_traversal_queue.dequeue()

			# if this parent has left child 
			if parent.left:
				
				# add this node in Queue	
				level_traversal_queue.enqueue(parent.left)
				
				# get the hd of left child ; child_hd = parent_hd - 1 
				left_child_hd = hd_of_nodes[parent]-1

				# add that hd in the map
				hd_of_nodes[parent.left] = left_child_hd

				# check if this Horizontal Distance Number key exits ; If not exists make it 
				if hd_group.get(left_child_hd) is None:
					# created new key with this left_child_hd Number
					hd_group[left_child_hd]=[]

				# add the left child in the group where he belongs	
				hd_group[left_child_hd].append(parent.left)	

			# if this parent has right child 
			if parent.right:
				
				# add this node in Queue	
				level_traversal_queue.enqueue(parent.right)
				
				# get the hd of right child ; child_hd = parent_hd + 1 
				right_child_hd = hd_of_nodes[parent] + 1

				# add that hd in the map
				hd_of_nodes[parent.right] = right_child_hd

				# check if this Horizontal Distance Number key exits ; If not exists make it 
				if hd_group.get(right_child_hd) is None:
					# created new key with this right_child_hd Number
					hd_group[right_child_hd]=[]

				# add the right child in the group where he belongs	
				hd_group[right_child_hd].append(parent.right)	
		
		for hd,group in hd_group.items():
			print(" %3d "%(hd),"  :  ",end="")
			for node in group:
				print(node,end="   ")
			print()	
						

tree = Tree()
tree.makeTree()

print(" -------------------- Vertical Order Traversal Traversal ------------------- ")
tree.verticalOrder()
print("\n","-"*50)

"""
					     27 
				  14     |      35
		      10     19  |   31	   42
		     9  12       | 29        90      

	
---------------------------------------------------
"""
"""
1) For Finding out Vertical Order Traversal we have to first take distance from any of the two side	
2) Horizontal Distance : Take Horizontal distance any of the two side . Left and Right 
                         It is distance from one side of tree 
3) For Root HD =0 
4) For Left Child HD = Parent Hd - 1
5) For Right Child HD = Parent Hd + 1

Level Order Traversal + Hash Table 

1) Enqueue Root
2) Update HD for root as 0 
3) Add Hd=0 in Hash Table and root as the value 
	REPEAT
4) Deqeue 
	i)  Check for left and right child and update Hd in Hash table
	ii) Enqueue the left and right child 
		
"""