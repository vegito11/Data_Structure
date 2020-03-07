# Algorithm
"""
	1) Remove loops and parallel edges  ( keep min weight )
	
	2) We require MinHeap/Priority Queue for this .

	3) Initiallize MinHeap+Hashing(hashMap) such that starting vertex weight is zero and other INIFINITY

	4) extract(pop) Min value that is root from MinHeap

	5) check its neighbour vertices and if distance to this neighbour is less than in MinHeap
	   decrease and also update this Edge in vertexEdge 

	6) After all neighbour is checked . remove next Min Edge Element from Heap 

	7) In the vertexEdge map check Who introduced this vertex . Add that edge in result

"""
from Weighted_Graph_Matrix import Graph as WeightedGraph
from binary_min_heap import BinaryMinHeap



class Primalgorithm:
	__INFINITY=9999999
	__VERTEXMAP={}

	def __init__(self,vertices_num):
		
		####### STEP 1) Create  a Graph and Initialize it which is similar in diagram ###   
		prim_graph = WeightedGraph(vertices_num)		
		Primalgorithm.__VERTEXMAP=(prim_graph.num_to_char_vertex)		
		self.createGraph(prim_graph)	

		##### STEP 2) Initiallize min Heap starting vertice will have weight zero and remaining to INIFINITY
		minHeap=self.initializeMinHeap(vertices_num)		
		Primalgorithm.showDetail(prim_graph,minHeap)

		Result=[]
		vertexEdgeMap={}

		# when heap is _isEmpty stop execution this loop 
		while not minHeap._isEmpty():

			# STEP 1) get the Minimun distanced node in graph (Pop Min)
			currentNode = minHeap.removeMin()

			## Add Edge correposing to this Vertex from vertexEdgeMap
			if currentNode.getKey() in vertexEdgeMap:
				Result.append(vertexEdgeMap[currentNode.getKey()])

			# print(cnt,minHeap._isEmpty(),minHeap)

			# get the Number representaion of current Node from CHARACTER to NUmber Mapping
			currentNodeNumber = Primalgorithm.__VERTEXMAP[currentNode.getKey()]
			currentNodeKey = currentNode.getKey()
			print(currentNodeKey)
			# as we get weight list we need interator which will give us correspoding weight vertex number
			i=0
			
			## STEP 2 ) Iterate over its all its neighbour
			edges=prim_graph.getEdgeList(currentNode.getKey())
			print(edges)
			# iterate over distance of source vertex to each vertex  
			for edgeWeight in edges:

				### STEP 2 This vertex is current vertex neighbour	
				# for this vertex if edges exist as weight is greater than 0
				if edgeWeight > 0:
					# print(edgeWeight,end=" ")
					# get character representation for this neighbour vertex number
					destinationVetexKey=self.getCharfromNumber(i)
					print(str(currentNodeKey+""+destinationVetexKey),edgeWeight)

					if destinationVetexKey not in minHeap.positionMap:
						# print("!!! ",destinationVetexKey,"!!!",minHeap.positionMap," ",currentNodeKey)	
						i+=1
						continue

					### STEP 3 ) Modify in heap if this distance is smaller
					# if distance to this Vertex i is less than it's previous distance in Heap 
					# then it will decrease and reheapify the Heap else unmodified
					if minHeap.getNode(destinationVetexKey) > edgeWeight:
						minHeap.decreaseNodeData(destinationVetexKey,edgeWeight)	
						vertexEdgeMap[destinationVetexKey]=str(currentNodeKey+""+destinationVetexKey)
				# increase vertex number
				i+=1
			print("--"*40)	

			# break
		print(vertexEdgeMap)
		print(Result)

	# it will return char representation of current number of Node		
	@staticmethod
	def getCharfromNumber(number):
		# list out keys and values separately 
		key_list = list(Primalgorithm.__VERTEXMAP.keys()) 
		val_list = list(Primalgorithm.__VERTEXMAP.values()) 		  
		# print(key_list[val_list.index(number)],end=" -- ")
		
		return key_list[val_list.index(number)]

	@staticmethod 
	def showDetail(prim_graph,minHeap):	
		prim_graph.graphInfo()
		print(Primalgorithm.__VERTEXMAP)
		print(prim_graph)
		print(minHeap)

	# this function will create Graph for our Example . we just have to give it WeightedGraph Object
	@staticmethod
	def createGraph(graph_ob):
		# (A,0) : (B,1) : (C,2) : (D,3)  : (E,4)  : (F,5) 
		graph_ob.addEdge("A","B",3)  # A -> B
		graph_ob.addEdge("A","D",1)  # A -> D
		graph_ob.addEdge("B","C",1)  # B -> C
		graph_ob.addEdge("B","D",3)  # B -> D
		graph_ob.addEdge("C","E",5)  # C -> E
		graph_ob.addEdge("C","F",4)  # C -> F
		graph_ob.addEdge("C","D",1)  # C -> D
		graph_ob.addEdge("D","E",6)  # D -> E
		graph_ob.addEdge("E","F",2)  # E -> F
	
	@staticmethod
	def initializeMinHeap(vertices_num):
		import random

		vertexMap=Primalgorithm.__VERTEXMAP
		# start from any random vertices
		value = random.randint(0,vertices_num-1)
		# value = 0
		
		# create BinaryMinHeap class object
		minHeap = BinaryMinHeap()
		
		# iterate over all vertices and then add it to heap	
		for vertice_key,number in vertexMap.items():
			
			# get any random vertice and make it weight zero and remaining infiinity
			if number==value:
				print(" Started from this vertice :  ",vertice_key)
				minHeap.addNode(vertice_key,0)
			else:
				minHeap.addNode(vertice_key,Primalgorithm.__INFINITY)
		return minHeap			

	def PrimMST(vertices_num):
		pass


# minHeap = BinaryMinHeap()

if __name__ == '__main__':
	Primalgorithm(6)

"""
1) start with one vertex 
2) choose edges which are made by this vertex . If these edge is minimum then add this in result
3) repeat this procedure
   
"""