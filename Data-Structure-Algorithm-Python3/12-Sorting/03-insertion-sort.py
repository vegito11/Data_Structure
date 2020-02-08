# when array is already sorted O(n) else 0(n*n)
from getArray import generateRandomArray

def insertion_sort(arr,type="asc"):
	
	# get length of array
	arr_len=len(arr)

	# Iterate length of array times
	for round in range(1,arr_len):

		# store current element in temporary variable
		current_element=arr[round]
		previous_index = round-1  #  increase by one when inserting element 

		""" if current_element is smaller than previous element insert in into its right position 
		ad move rest element to right by one step  """

		while previous_index>=0 and current_element < arr[previous_index]:
			# shift the element to right by one step . that to its neighbour
			tmp=arr[previous_index]
			arr[previous_index]=arr[previous_index+1]
			arr[previous_index+1]=tmp
			# move to left of array for further checking (we will increase it by one when loop end)
			previous_index=previous_index-1

		# as we decrease previous_index in each step for checking at left side  . 
		# we have to increase to insert current element at its right position
		previous_index+=1	
		# place current element in its right position	
		arr[previous_index]=current_element	

		# print(arr) ######

if __name__ == '__main__':
	array=generateRandomArray(4)
	print("Before Sort : ",array)
	insertion_sort(array)
	print("After Sort  : ",array)

"""
Algorithm : Ascending (smallest to largest)

	1) We start from second element that is index 1 
	2) At each round start we have sorted array till (round-1) position
	3) We compare the current element (arr[round]) to previous element 
		3.1) If element previous element is not smaller than current elememnt then 
		     search for current element position in till round index (0,round-1) . 
		     insert current element in that position and shift rest element by 1 place to right 
		3.2) Else do not do anything

"""	