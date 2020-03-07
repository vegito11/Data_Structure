class Graph:
	
	def __init__(self,vertices=4):
		self.vertices = vertices
		self.edges = 0
		self.addMatrix=[]

		# create 2D Array . each dimensions are vertice X vertice
		for vertice in range(self.vertices):
			# for each vertice add new list with [0,0,0,0,...,vertice]
			self.addMatrix.append([0 for num in range(vertices)])

	def addEdge(self,source_vertex,destination_vertex):
		
		# if index out of range then return without any action
		if source_vertex >= self.vertices or destination_vertex >= self.vertices: return
		
		# if this edges already exist then don't' it 	
		if self.addMatrix[source_vertex][destination_vertex]==1: return	 
		
		# mark the one in 1 in Matrix for [v1][v2]
		self.addMatrix[source_vertex][destination_vertex]=1	
		# this edge is bidirection hence mark edge also in reverse direction
		self.addMatrix[destination_vertex][source_vertex]=1	
		# increase the number of edges 
		self.edges+=1

	def removeEdge(self,source_vertex,destination_vertex):

		# if index out of range then return without any action
		if source_vertex >= self.vertices or destination_vertex >= self.vertices: return

		# if this edges doesnt exist then don't do anything
		if self.addMatrix[source_vertex][destination_vertex]==0: return	 

		# mark the one in 0 in Matrix for [v1][v2]
		self.addMatrix[source_vertex][destination_vertex]=0	
		
		# this edge is bidirection hence remove edge also in reverse direction
		self.addMatrix[destination_vertex][source_vertex]=0
		# decrease the number of edges
		self.edges-=1
	
	def graphInfo(self):
		print(" Number of vertices of Graph are ",self.vertices)
		print(" Number of Edges of Graph are ",self.edges)

	def __str__(self):
		for row in self.addMatrix:			
			print("\n",end="   ")	
			for val in row:
				print(val,end="  ")
		print()
		return " "

graph = Graph(5)
graph.graphInfo()
graph.addEdge(1,3)
graph.addEdge(2,4)
graph.addEdge(4,0)
graph.addEdge(7,9)
print(graph)
graph.graphInfo()