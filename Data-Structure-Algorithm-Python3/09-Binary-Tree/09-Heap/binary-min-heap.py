# Priority Queue
# removeMin 		 :  O(log n)
# addNewNode	 	 :  O(log n)
# contains	         :  O(1)
# decreaseNodeValue  :  O(log n)
# increaseNodeValue  :  O(log n)
class Node:

	def __init__(self,name,key):
		self.name=name
		self.weight=key
	
	def __str__(self):
		return  self.name+" "+str(self.weight)
	
	def getData(self):
		return self.weight

	def setData(self,newWeight):
		self.weight=newWeight

	def getKey(self):
		return self.name

# Root node is smallest data Node in Heap and all the children are greater than Parent
class BinaryMinHeap:
	"""
		- size will give the number of node in Heap . 
		- allNodeList is Private Member and it is heap array which will contain all the node .
		- positionMap it is dictionary which will give us key Position of node with given key 
		  in that List . 

	"""
	def __init__(self):
		self.size=0
		self._allNodeList=[]
		self.positionMap={}

	# swap two node in the Heap		
	def swapNode(self,currentIndex,parentIndex):
		tmp=self._allNodeList[parentIndex]
		self._allNodeList[parentIndex]=self._allNodeList[currentIndex]
		self._allNodeList[currentIndex]=tmp
	
	# return True if data at index1 is greater than data at index2 else False	
	def isGreater(self,index1,index2):
		try:
			if self._allNodeList[index1].getData() >= self._allNodeList[index2].getData():
				return True
			else:
				return False	
		except Exception as e:
			print(e)

		self._allNodeList

	# it will add the node in the Heap and also update the positionMap 	
	def addNode(self,name,weight):
		
		# create new Node which we are going to add in List 
		newNode=Node(name,weight)

		# add the new Node in List 
		self._allNodeList.append(newNode)

		# increase size of list 
		self.size+=1

		# add this new Node key and its value as its positon in List 
		self.positionMap[newNode.getKey()]=self.size-1

		# get the Index of last Node in heap
		currentIndex=self.size-1

		# get the Index of Parent of this child  If child is Root . parent =-1 break
		parentIndex=(currentIndex-1)//2

		# Run this loop until we come back to Root of Node or break if condition fail
		while parentIndex>=0:

			# if Parent data is greater than child data then swap this nodes
			if self.isGreater(parentIndex,currentIndex):

				# swap the index of those key in positionMap
				self.positionMap.update({
					self._allNodeList[currentIndex].getKey():parentIndex,
					self._allNodeList[parentIndex].getKey():currentIndex})

				# swap this two nodes 
				self.swapNode(parentIndex,currentIndex)


				# now go up my making currentIndex to parentIndex
				currentIndex=parentIndex

				# get the Index of Parent of this child 
				parentIndex=(currentIndex-1)//2
			
			# break if parentNode key is not greater than child Node key	
			else:
				break;

	# it will remove first element and reheapify the Heap
	def removeMin(self):

		# if heap is _isEmpty then return without doing anything
		if self._isEmpty():	return None

		# 1) get first Node from Heap	
		min=self._allNodeList[0]

		# remove this first element from positionMap		
		self.positionMap.pop(min.getKey())


		# 2) remove the last element from the heap
		last=self._allNodeList.pop()

		# 3) decrease size of Heap
		self.size-=1

		# if heap is _isEmpty then return without doing anything
		if self._isEmpty():	return None

		# replace last element as a new Root
		self._allNodeList[0]=last

		# also in positionMap make this node as firstNode
		self.positionMap[last.getKey()]=0


		parentIndex=0
		leftChildIndex  = 2 * parentIndex + 1
		rightChildIndex = 2 * parentIndex + 2

		# 4) Run until leftChild exists and if condition satisfy
		while leftChildIndex < self.size:
			
			# if parent do not have rightChild then check only left child 
			if rightChildIndex >=self.size:

				# if child have minimum value than parent 
				if self.isGreater(parentIndex,leftChildIndex):
					# swap the index of those key in positionMap
					self.positionMap.update({
						self._allNodeList[parentIndex].getKey():leftChildIndex,
						self._allNodeList[leftChildIndex].getKey():parentIndex})
					
					# make left child new parent 
					self.swapNode(parentIndex,leftChildIndex)

				break	

			# 5) if parent (0) data is greater than child(1 or 2 ) then swap which child is smaller
			if self.isGreater(parentIndex,leftChildIndex) or self.isGreater(parentIndex,rightChildIndex):

				# if left child is greater than right child 	
				if self.isGreater(rightChildIndex,leftChildIndex):
					
					# swap the index of those key in positionMap
					self.positionMap.update({
						self._allNodeList[parentIndex].getKey():leftChildIndex,
						self._allNodeList[leftChildIndex].getKey():parentIndex})
	
					# make left child new parent 
					self.swapNode(parentIndex,leftChildIndex)

					# now go to leftChildIndex start checking if this node fits here or not
					parentIndex=leftChildIndex

				# if rightChild is greater than left Child 
				else:
				
					# swap the index of those key in positionMap
					self.positionMap.update({
						self._allNodeList[parentIndex].getKey():rightChildIndex,
						self._allNodeList[rightChildIndex].getKey():parentIndex})
	
					# make right child new parent 
					self.swapNode(parentIndex,rightChildIndex)
					
					# now go to rightChildIndex start checking if this node fits here or not
					parentIndex=rightChildIndex

				leftChildIndex  = 2 * parentIndex + 1
				rightChildIndex = 2 * parentIndex + 2

			# if parentIndex element right fit
			else:	
				break;

		return min	

	# if heap is _isEmpty then return without doing anything
	def _isEmpty(self):
		if len(self._allNodeList)<=0:
			return True
		return False	
	
	# decrease the Node in the Heap	
	def decreaseNodeData(self,key,newData):
		
		# get the position of key
		keyIndex = self.positionMap[key]

		self._allNodeList[keyIndex].setData(newData)

		# Get the Parent Index 
		parentIndex = (keyIndex-1)//2

		while parentIndex >= 0 :
			# if keyIndex(child) data is minimum than parent . swap 
			if self.isGreater(parentIndex,keyIndex):
				# swap the index of those key in positionMap
				self.positionMap.update({
					self._allNodeList[parentIndex].getKey():keyIndex,
					self._allNodeList[keyIndex].getKey():parentIndex})
				
				self.swapNode(parentIndex,keyIndex)

				keyIndex=parentIndex
				parentIndex = (keyIndex-1)//2
			else:
				break	

	# decrease the Node in the Heap	
	def increaseNodeData(self,key,newData):
		
		# get the position of key
		keyIndex = self.positionMap[key]

		self._allNodeList[keyIndex].setData(newData)

		parentIndex=keyIndex
		leftChildIndex  = 2 * parentIndex + 1
		rightChildIndex = 2 * parentIndex + 2

		# 4) Run until leftChild exists and if condition satisfy
		while leftChildIndex < self.size:
			
			# if parent do not have rightChild then check only left child 
			if rightChildIndex >=self.size:

				# if child have minimum value than parent 
				if self.isGreater(parentIndex,leftChildIndex):
					# swap the index of those key in positionMap
					self.positionMap.update({
						self._allNodeList[parentIndex].getKey():leftChildIndex,
						self._allNodeList[leftChildIndex].getKey():parentIndex})
					
					# make left child new parent 
					self.swapNode(parentIndex,leftChildIndex)

				break	

			# 5) if parent (0) data is greater than child(1 or 2 ) then swap which child is smaller
			if self.isGreater(parentIndex,leftChildIndex) or self.isGreater(parentIndex,rightChildIndex):

				# if left child is greater than right child 	
				if self.isGreater(rightChildIndex,leftChildIndex):
					childIndex=leftChildIndex
				else:	
					childIndex=rightChildIndex

				# swap the index of those key in positionMap
				self.positionMap.update({
					self._allNodeList[parentIndex].getKey():childIndex,
					self._allNodeList[childIndex].getKey():parentIndex})
	
				# make left child new parent 
				self.swapNode(parentIndex,childIndex)

				# now go to childIndex start checking if this node fits here or not
				parentIndex=childIndex

				leftChildIndex  = 2 * parentIndex + 1
				rightChildIndex = 2 * parentIndex + 2

			# if parentIndex element right fit
			else:	
				break;

	def printBinaryHeap(self):
		for i in self._allNodeList:
			print(i,end=" | ")
		print("\n","--"*40)	


heap=BinaryMinHeap()	
heap.addNode("Omkar",12)
heap.addNode("vegito",3)
heap.addNode("neymar",33)
heap.addNode("coutiniho",8)
heap.addNode("leo",79)
heap.addNode("mane",2)

heap.printBinaryHeap()
print(heap.positionMap)

print(heap.removeMin())
heap.printBinaryHeap()
print(heap.positionMap)

print("*"*80)
print(heap.decreaseNodeData("Omkar",1))
heap.printBinaryHeap()
print(heap.positionMap)

print("*.."*20)
heap.increaseNodeData("Omkar",145)
heap.increaseNodeData("vegito",845)
heap.printBinaryHeap()
print(heap.positionMap)



"""
	parent = floor(index/2)    If start is 1

	parent = floor(index-1/2)    If start is 0
		left  child : ( 2 * i  +  1 )
		right child : ( 2 * i  +  2 )

					 0
				1 	  	    2
			3	  4     5       6

"""