## Linked List 

.Each node is represnted as a unique object , with that instance storing a reference to 
 its element and a reference to the next node (or None)
.An Property of LL is that it does not have a predetermined fixed size

Pros : 
	1) Linked List have constant time insertion and deletion in any position,
	   comparison, arrays require O(n) time to the same thing 
	2) Linked list can continue to expand without having to specify their size ahead of 
	   time 

Cons:
	1) To access an element in a linked list , you need to take O(k) time to 
	   go from the head of the list to the kth element 

Note : 

	1) During removal we have to store previous node address so that we can 
	   remove current node 
	2) For removal 
		tmp = None   
		del tmp