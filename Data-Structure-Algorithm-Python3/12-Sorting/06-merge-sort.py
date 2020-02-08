# 1) Stable
# 2) Θ(n) extra space for arrays (as shown)
# 3) Θ(lg(n)) extra space for linked lists
# 4) Θ(n·lg(n)) time
# 5) Not adaptive
# 6) Does not require random access to data

from getArray import generateRandomArray

# First array will start from startIndex till middle_index | second array will start from middle_index+1 till endIndex
def merge(original_array,startIndex,middle_index,endIndex):
	
	# size of first array 
	left_size = middle_index - startIndex + 1
	
	# size of second array 
	right_size = endIndex - middle_index
	
	# create two array of this size
	left_array  = [0]*left_size
	# create two array of this size
	right_array = [0]*right_size

	# copy data of original_array into left array 
	for inc in range(left_size):
		# as original_array will not start from 0 we have to increment from offset which is startIndex
		left_array[inc]=original_array[startIndex+inc]

	# copy data of original_array into right array 
	for inc in range(right_size):
		# as original_array will not start from 0 we have to increment from offset which is middle_index+1
		right_array[inc]=original_array[middle_index+1+inc]
	
	# print(left_array,"--",right_array)	

	# Now we have to compare element from left and right array and place into whichever element is smaller 
	# in original_array at its position
	left_itr=0
	right_itr=0
	original_array_itr=startIndex

	while left_itr<left_size and right_itr<right_size:
		# if element in left array is smaller then this will place in original_array
		if left_array[left_itr] < right_array[right_itr] :
			original_array[original_array_itr] = left_array[left_itr]
			left_itr+=1
			original_array_itr+=1
		# if element in right array is smaller then this will place in original_array
		else:	
			original_array[original_array_itr] = right_array[right_itr]
			right_itr+=1
			original_array_itr+=1

	# if left_array still contain some elements then place this element in this array
	while left_itr < left_size:		
		original_array[original_array_itr] = left_array[left_itr]
		left_itr+=1
		original_array_itr+=1

	# if right_array still contain some elements then place this element in this array
	while right_itr < right_size:		
		original_array[original_array_itr] = right_array[right_itr]
		right_itr+=1
		original_array_itr+=1

def merge_sort(array,startIndex,endIndex):
	
	if startIndex < endIndex:
		# 0 , 7 = 3 | 0-3 and 4-7
		# 0 , 6 = 3 | 0-3 and 4-6
		# 0 , 1 = 3 | 0-3 and 4-6
		middle_index = (startIndex+endIndex)//2

		# first sort left half 
		merge_sort(array,startIndex,middle_index)
		
		# then sort second half 
		merge_sort(array,middle_index+1,endIndex)

		# Now merge this two sorted Arrays
		merge(array,startIndex,middle_index,endIndex)

if __name__ == '__main__':
	array=generateRandomArray(7)
	print("Before Sort : ",array)
	merge_sort(array,0,len(array)-1)
	print("After Sort  : ",array)


# 1) In merge sort will first divide all the arrays in high
# 2) At then end we merge which is started from 1,1 array 
# 3) then they are merge