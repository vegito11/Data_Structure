from getArray import generateRandomArray

def swap(arr,index1,index2): arr[index1],arr[index2]=arr[index2],arr[index1]
def selection_sort(arr,type="asc"):
	
	# get length of array
	arr_len=len(arr)

	# Iterate length of array times
	for round in range(arr_len):
		
		# Compare current element with remaining element (i-N) [1-5] [2-5] [3-5]
		for ind2 in range(round+1,arr_len):
			
			# if current element is greater than other element then put this smaller element at this position
			if type=="asc" and arr[round] > arr[ind2]:
				swap(arr,ind2,round)

			if type!="asc" and arr[round] < arr[ind2]:
				swap(arr,ind2,round)
		print(arr)   ########
		
	print("-"*40)		

if __name__ == '__main__':
	array=generateRandomArray(7)
	print("Before Sort : ",array)
	selection_sort(array)
	print("After Sort  : ",array)
	print("__"*40)
	print("Before Sort : ",array)
	selection_sort(array,"desc")
	print("After Sort  : ",array)

"""
Algorithm : 

	1) Each round we select round-th smallest element at place it in this position 
	2) At Each iteraton ( n ) we place smallest element at its last place (ind1)
	3) in next step we interate from ind1+1 to n element
"""	