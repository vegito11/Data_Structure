## Circular List 

	Travelling to last node 

	current.next!=self.head

1) Add(item) : 
	
	a) start : when adding node to end of list . travel till current.next == start

2) Remove() : 
	
	a) start :  delete first node and make 2nd node as new First node
				travel to last node make it point to the new start node

3) Display() : 
	
	a) travel till last node . in loop print all nodes 
	b) print last node outside loop

