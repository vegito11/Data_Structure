class Graph:
	
	def __init__(self,vertices=4):
		CHARS=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
		self.vertices = vertices
		self.edges = 0
		self.addMatrix=[]
		self.num_to_char_vertex={}
		# create 2D Array . each dimensions are vertice X vertice
		for vertice in range(self.vertices):
			# for each vertice add new list with [0,0,0,0,...,vertice]
			self.addMatrix.append([0 for num in range(vertices)])
			self.num_to_char_vertex.update({CHARS[vertice]:vertice})
	
	def addEdge(self,source_vertex,destination_vertex,weight):
		"""
			give argument source_vertex , destination vertex and weight of edge between them 
			source_vertex start from 0 upto v-1
		"""	
		# if we do not given number as veritice and given char as vertice name convert it to number
		if type(source_vertex)==str:
			source_vertex=self.num_to_char_vertex[source_vertex]
			destination_vertex=self.num_to_char_vertex[destination_vertex]
		# if index out of range then return without any action
		if source_vertex >= self.vertices or destination_vertex >= self.vertices: return
		
		# if this edges already exist then don't' it 	
		if self.addMatrix[source_vertex][destination_vertex]>=1: return	 
		
		# mark the one in 1 in Matrix for [v1][v2]
		self.addMatrix[source_vertex][destination_vertex]=weight
		# this edge is bidirection hence mark edge also in reverse direction
		self.addMatrix[destination_vertex][source_vertex]=weight	
		# increase the number of edges 
		self.edges+=1

	def removeEdge(self,source_vertex,destination_vertex):

		# if we do not given number as veritice and given char as vertice name convert it to number
		if type(source_vertex)==str:
			source_vertex=self.num_to_char_vertex(source_vertex)
			destination_vertex=self.num_to_char_vertex(destination_vertex)

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
		print(self.num_to_char_vertex)

	def getEdgeList(self,source_vertex):

		# if we do not given number as veritice and given char as vertice name convert it to number
		if type(source_vertex)==str:
			source_vertex=self.num_to_char_vertex[source_vertex]

		# if index out of range then return without any action
		if source_vertex >= self.vertices : return

		# it wil return list which contain distance from this node to all other node in graph
		return self.addMatrix[source_vertex]

	def __str__(self):
		for row in self.addMatrix:			
			print("\n",end="   ")	
			for val in row:
				print(val,end="  ")
		print()
		return " "

# this will not run when we impott this module . it will run this only when we run this file directly
if __name__ == '__main__':
	print("END")
