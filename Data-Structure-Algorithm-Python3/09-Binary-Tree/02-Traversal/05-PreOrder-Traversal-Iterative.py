from Stack import Stack
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
	def insert(self,data):
				
		newNode=Node(data)
				
		if self.root==None:
			self.root=newNode
			return

		current=self.root	
		while current!=None:
			
			if current.key>data:
								
				if current.left==None:
					current.left=newNode
					return				
				else:
					current=current.left
						
			elif current.key<data:
								
				if current.right==None:
					current.right=newNode
					return				
				else:
					current=current.right			
			else:
				return		

	## preorder traversal (Root First , Left and Then Right) 
	def preorder(self):
		# get the root address in variable 
		root = self.root
		# if tree doesn't contain any data 
		if root==None:
			return
		else:
			# create new Stack which will store right subtree root which will be require when we 
			# once traversed left and root of subtree
			stackRight = Stack()

			# break when stackRight is Empty
			while True:
				# if root is not Empty print it 
				if root is not None:
					print(root,end=" - ")
					# push right subtree which will be processed after left is processed 
					stackRight.push(root.right)
					# go to process left subtree
					root=root.left
				else:
					if stackRight.isEmpty():
						return
					# not right subtree is processed pop right subtree which we have pushed	
					root=stackRight.pop()	



tree = Tree()
st = Stack()
st.push(10)
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
# Root Left Right
print("Root Left Right")
print("Preorder Traversal: ",end="")
head = tree.preorder()
print("\n","-"*50)

"""
					     27 
				  14     |      35
		      10     19  |   31	   42
		     9  12       | 29        90      

	MLR:  27__14__10__9__12__19__35__31__29__42__90__
---------------------------------------------------
"""
""" 
	1) print root push its right in stack
	2) move to its left by making left node as new root 
	3) If root is node pop from stack (right subtree which we have inserted)
"""