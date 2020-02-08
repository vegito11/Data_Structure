## Queue : 
	
	. The Queue abstract data type os defined by the following structure and operation .
	. A Queue is strcutured as described above , as an orderred collection of items where 
	  items added to one end called "rear " removed from the another end called "front".
	. Queues are ordered FIFO . 

## Queue Operations :
	
	Queue() : create new Queue 

	enqueue(item) : returns nothing
	
	dequeue() : returns item

	isEmpty() : 

	size() : 

## 	Deque : Double Ended Queue
	
	. A dequeue, also known as Double-ended queue 
	. It is an ordered collection of items similar to the queue 
	. It has two ends , a front and a rear and the items remain positioned in 
	  the collections
	
	Queue() : create new Queue 

	addFront(item) : returns nothing
	
	addRear(item) : returns nothing
	
	RemoveFront() : returns item
	
	RemoveRear() : returns item

	isEmpty() : 
	
	size() : 


	* Note : 
		- It is important to note that even though the dequeu can assume many of the characterstics 
		  of stacks and queue . It doesnt require the LIFO and FIFO orderings that are enforced 
		  by those data strucutures
		- It is up tp make consistent use of the addition and removal operations  