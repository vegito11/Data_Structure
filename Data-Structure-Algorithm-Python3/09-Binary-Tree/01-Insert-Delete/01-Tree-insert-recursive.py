# Complexity O(H) where h is height of BST
class Node:
	# constructor take name and age as argument and create new Node
	def __init__(self,data):
		self.key=data
		self.left=None
		self.right=None

	def __str__(self):		
		return f'{self.key}'

class Tree:
	def __init__(self):
		self.root = None

	# classmethod so that we can is recurssively call this method 
	@classmethod	
	def insertData(cls,tree,data):

		# if new node pass is empty like 30.left==None passed to function insertData(root.left)
		if tree==None:
			newNode = Node(data)
			# return newly created Node  
			return newNode

		# if new element is less than root of current tree insert it to the left of that tree	
		elif tree.key>data:
			# if subtree.left contain data it will return its left address if empty it will 
			# point to new Node

			tree.left=cls.insertData(tree.left,data)

		# if new element is greater than root of current tree insert it to the left of that tree	
		elif tree.key<data:
			tree.right=cls.insertData(tree.right,data)

		# at each step return tree . first recurssion result is self.root other 
		# is whatever we have passed root.left or root.right
		return tree	

	# call insertData method which is recurssive method 	
	def insert(self,data):
		self.root=self.insertData(self.root,data)
		print(self.root,end="----------")

tree = Tree()
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(80)
print()
print(tree.root.right)
print(tree.root.left)
