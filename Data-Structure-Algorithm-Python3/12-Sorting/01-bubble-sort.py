from getArray import generateRandomArray

def swap(arr,index1,index2): arr[index1],arr[index2]=arr[index2],arr[index1]
def bubbleSort(arr,type="asc"):
	
	# get length of array
	arr_len=len(arr)

	# Iterate length of array times
	for round in range(arr_len):
		
		# If there is no swapping occure in one n pass round then array is sorted 
		is_swapped=False

		# Compare current element with remaining element (n-i) [1,5] , [1-4] , [1-3] , [1-2]
		for ind2 in range(arr_len-round-1):
			
			# if current element is greater than its neighbour then swap them
			if type=="asc" and arr[ind2] > arr[ind2+1]:
				swap(arr,ind2,ind2+1)
				is_swapped=True

			if type!="asc" and arr[ind2] < arr[ind2+1]:
				swap(arr,ind2,ind2+1)
				is_swapped=True

		print(arr)  ######
		
		# if not swapping happen in last round then Array is Sorted break out of while		
		if is_swapped==False: break		
	print("-"*40)		
			

if __name__ == '__main__':
	array=generateRandomArray(5)
	print("Before Sort : ",array)
	bubbleSort(array)
	print("After Sort  : ",array)
	print("__"*40)
	print("Before Sort : ",array)
	bubbleSort(array,"desc")
	print("After Sort  : ",array)


"""
Algorithm : 

	1) Outer loop is just for iteration n times thats it 
	2) Inner Loop will compare neightbour always starting from 1 index 
	3) We compare 1,2 | 2,3 | 3,4 | 4,5 | 5,6
	3) After each round we will put greatest element at last position (n) PS n-i
"""	