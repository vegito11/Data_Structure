============================================= Tree ================================================
01] Tree : 

	1) Root : The node at the top of the tree is called root. 
			  There is only one root per tree and one path from the root node to any node.

	2) Parent − Any node except the root node has one edge upward to a node called parent.

	3) Child − The node below a given node connected by its edge downward is called its child node.

	4) Leaf − The node which does not have any child node is called the leaf node.

	5) Subtree − Subtree represents the descendants of a node.

	6) Traversing − Traversing means passing through nodes in a specific order.

	7) Levels − Level of a node represents the generation of a node.
	            
	            If the root node is at level 0, then its next child node is at level 1, 
	            its grandchild is at level 2, and so on.

___________________________________________________________________________________________________

02] BST : 
	
	1) Binary Search tree exhibits a special behavior. 
	2) A node's left child must have a value less than its parent's value and the node's right
	   child must have a value greater than its parent value
							
						  27 
					14 	  |   35
			      10  19  | 31	42
	---------------------------------------------------
	Insert − Inserts an element in a tree/create a tree.

	Search − Searches an element in a tree.

	Preorder Traversal − Traverses a tree in a pre-order manner.

	Inorder Traversal − Traverses a tree in an in-order manner.

	Postorder Traversal − Traverses a tree in a post-order manner.		      
___________________________________________________________________________________________________

03] Traversal : 
	
	1) InOrder   : Left ,	Root ,  Right . Gives sorted result 
	2) PreOrder  : First Root , Left , Right
	3) PostOrder : First Left , Right , Root

___________________________________________________________________________________________________

04] Tree Recursion Trick : 
	
	1) Always minimize the problem 
	2) delegate problem to subtree 
	3) Think solution for  1 Node or 3 Node (only 2 children tree)

	Example : 
	
	1) For Diameter parent diameter will diameter of of children
	2) For Check Mirror if child is mirror parent will be mirror
		if Tree.checkMirror(tree1.left,tree2.right) and Tree.checkMirror(tree1.right,tree2.left):
	3) For height : let child calculate there height answer will be max between left and right child
___________________________________________________________________________________________________