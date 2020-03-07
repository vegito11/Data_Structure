# refer below link for magic method information
# https://rszalski.github.io/magicmethods/#appendix1
import ctypes

class DynamicArray(object):

	# 01-constructor when we first Initiallize Array/Class
	def __init__(self):
		self.n = 0 
		self.capacity = 1 
		self.A = self.make_array(self.capacity)

	# 02-Special Method we can use it like len(object)	
	def __len__(self):
		return self.n

	# 03-Special method called when use subscript ob[0]	
	def __getitem__(self,index):
		try:
			if index < 0  or index > self.capacity:
				raise IndexError()
			else:	
				return self.A[k]
		except Exception as e:
			print("Index out of Bound")
			return None

	# 04-method to add element in array 
	def append(self,ele):
		
		# if Array is full increase capacity of this arrary 
		if self.n == self.capacity:
			print("------------- Resizing ------------- ")
			self._resize(2*self.capacity)

		self.A[self.n]=ele 
		self.n+=1

	# 05-private method bcz `_`only we can access inside this class 
	def _resize(self,new_capacity):

		# Make new array whose capacity is greter than previous one 
		B = self.make_array(new_capacity)
		
		# Copy data from previous array to this array
		for k in range(self.n):
			B[k]=self.A[k]

		# Points Old array to this new array with new capacity
		self.A = B
		self.capacity = new_capacity

	def make_array(self,new_capacity):
		return (new_capacity * ctypes.py_object)()

arr = DynamicArray()

# arr.append(1)
# print(len(arr))
for i in range(1,52):
	
	# Number of elements
	length = len(arr)

	# Actual Size in Bytes 
	size = arr.capacity

	print(f' Length: {length:3d} ; Size in bytes: {size:4d}')

	# increase length by one
	arr.append(i)