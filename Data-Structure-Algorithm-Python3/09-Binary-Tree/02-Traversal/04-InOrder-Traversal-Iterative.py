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

	## inorder traversal (it gives Sorted list) 
	# First Print Left , then Root and then Right 
	def inorder(self):
		# get the root address in variable 
		root = self.root
		# if tree doesn't contain any data 
		if root==None:
			return
		else:
			# create new Stack 
			stackLeft = Stack()
			while True:
			
				# move to left of current subtree until we GO to END of this subtree (NONE)
				# if current subtree is not leaf push it in stack and move to its *Left subtree
				if root!=None:

					# push current subtree to stack for further processing
					stackLeft.push(root)
					# move to left subtree of current subtree for processing
					root=root.left
				
				# if all left subtree of current subtree pushed and we are at leaf node 
				else:	
					# if stack is empty end the function
					if stackLeft.isEmpty():
						break
					# current root is empty So get the Last Pushed subtree root on Stack	
					root=stackLeft.pop()
					print(root,end=" - ")
					# when processed left go to rigth subtree it will repeat process of processing 
					# its left nodes and then process this subtree
					root=root.right
						

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
print(tree.root)
print("Inorder Traversal: ",end="")
head = tree.inorder()
print("\n","-"*50)

"""
					     27 
				  14     |      35
		      10     19  |   31	   42
		     9  12       | 29        90      

	LMR:  9__10__12__14__19__27__29__31__35__42__90__
---------------------------------------------------
"""

"""
	Push(9)
	Then None 
	Pop(9)
	Then None 
	Pop(10)
	Then Push(12)

"""
"""
	push root in stack 
	and make new root=root.left that is traverse left side
	Repeat this until we reach end of left subtree that is None
	
	Now once we get None pop element from tree to process and travel its right side 
	and process it like above
"""