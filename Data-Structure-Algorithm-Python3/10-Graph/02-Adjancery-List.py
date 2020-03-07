class Graph:
	
	def __init__(self,vertices=4):
		
		self.vertices = vertices		
		self._VNAMES=["A","B","C","D","E","F","G","H"]
		self.edges = 0

		# this is map which have key as Vertex Name and value is set of its edges
		self.graphMap={}
		self._initiallizeGraph(vertices)

	def _initiallizeGraph(self,vertices):
		
		# add KEY to Map where value of each KEY is empty SET()
		for i in range(vertices):
			self.graphMap[self._VNAMES[i]]=set()

	def addEdge(self,source_vertex,destination_vertex):
		
		# If that source and destination vertex already exists then do not do anything
		if source_vertex not in self._VNAMES and destination_vertex not in self._VNAMES:
			return
		if destination_vertex in self.graphMap[source_vertex]: return
		
		# add this destination_vertex in the set where key is source_vertex
		self.graphMap[source_vertex].add(destination_vertex)
		self.graphMap[destination_vertex].add(source_vertex)
		
		self.edges+=1

	def removeEdge(self,source_vertex,destination_vertex):

		# If that source and destination vertex are not give List of Vertex
		if source_vertex not in self._VNAMES and destination_vertex not in self._VNAMES:
			return
		
		# if that vertices does not exist in then edge will not exist 
		if destination_vertex not in self.graphMap[source_vertex]: return

		# remove that edge 
		self.graphMap[source_vertex].discard(destination_vertex)
		self.graphMap[destination_vertex].discard(source_vertex)

		self.edges-=1
	
	def graphInfo(self):
		print(" Number of vertices of Graph are ",self.vertices)
		print(" Number of Edges of Graph are ",self.edges)

	def __str__(self):
		for source,destination_vertices in self.graphMap.items():
			print(source,":",end=" ")
			for destination in destination_vertices:
				print(source," => ",destination,end=" , ")
			print()	
		return ""

graph = Graph(5)
graph.addEdge("A","B")
graph.addEdge("A","C")
graph.addEdge("A","C")
graph.addEdge("A","D")

print(graph)
graph.graphInfo()

graph.removeEdge("A","C")
graph.removeEdge("A","D")

print(graph)
graph.graphInfo()