 =============================================== Graph =====================================================
1) Graph : 
	
	- Graphs are a more general structure than trees . we can think of a tree as a special kind of graph 
	- Graph can be used to represent many real-word things such as system of roads , airline flights 
	  from city to city , how the internet is connected 
	- Once we have a good representation for a problem , we can use some standard graph algorithm 
	  to solve what otherwise might seem to be a very difficult problem 
___________________________________________________________________________________________________________

2) Terms in Graphs : 
	
	a) Vertex : also called as Node and are fundamental part of Graph 
				It also has additional Information we call this as payload 
	b) Edge   : An Edge connect two vertices to show that there is a relationship between them 
				. Edge can be one way or two way  
				. If All edges are one way then we called it Digraph or Directed Graph

	--------------------------------------------------------------

	* A graph can be represented by G where G = (V,E)
	* For the graph G,V is a set of vertices and E is a set of Edges 
	* Each edge is a tuple (v,w) where w,v E V 
	* We can add a third component to the edge tuple to represent a weight 
	* A subgraph S is set of Edges e and Vertices V such that e E E and v E V 

	Order of Graph = |V| = Number of Vertices
	Size of Graph  = |E| = Number of Edges
___________________________________________________________________________________________________________

3) Graph Representation : 
	
	a) Matrix Representation : 
	
		Space Complexity :  O(v^2)

		Time Complexity for : insert,delete,search  O(1)

	b) Adjancery List Representaion : 
	
		Space Complexity :  O(v+e)

		Time Complexity for : insert,delete,search  O(v+e)
___________________________________________________________________________________________________________

4) Degree of Vertex : Number of  edges incident on a vertex
	
	a) Undirected Graph : 
		- degree 0 is isolated.
		- loop edge

	b) Directed Graph : 
		
		Indegree   -  Number of edges going toward this edge
		OutDegree  -  Number of edges going away from this vertex
		Loop Edges -  1 Indgree + 1 outDegree
___________________________________________________________________________________________________________

5) Classes of Graph : 
	
	a) Regular graph  : Each vertex degree is same 
	b) complete graph : Every vertex each connected to every other vertex in graph  
	
	c) connected graph undirected : from every vertex there is path to reach every another vertex
	c) strongely connected graph  : from every vertex there is path to reach every another vertex
	
	d) planar graph   :  no to edges should intersect each other 
	e) bipatite graph : vertices divide in two group . every vertex in one group is connected to every 
	                    vertex in another group
	f) tree           : connected graph with no cycle                    
___________________________________________________________________________________________________________

6) BFS and DFS Traversal in Graph : 
	
	A] BFS : 

		a) We required one Queue and one Array whose size is number of vertices 
		b) we enqueue root first/or any one node 
		c) Then repeat below procedure until Queue is not empty 

		d) dequeue the node from queue . print that NODE 
		e) enqueue all of its connected nodes  (which are not visited)
		f) and mark the flag in VISITED array 
	
	B] DFS : 

		a) We required one Stack and one Array whose size is number of vertices 
		b) we push root first/or any one node 
		c) Then repeat below procedure until Stack is not empty 

		d) we print when we push the node in stack 
		e) now get the TOP the of the stack 
		f) Push ONE of its  adjancent Node if not visited . Mark that pushed node in VISITED array 
		g) Remove/POP from stack only when current node do not have any adjancet UNVISITED vertices
		h) repeat this procedure 
		----------------------------------------------------------
		Remember : Push only one of the adjacent Node if not visited 	



___________________________________________________________________________________________________________

10] Reference : 
	
	https://www.programiz.com/dsa/graph-adjacency-matrix

___________________________________________________________________________________________________________