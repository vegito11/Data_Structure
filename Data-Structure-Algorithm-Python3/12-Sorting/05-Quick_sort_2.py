# 1) Let maintain two pointers One where last swap happend and one is moving toward right 
# 2) We select last element as pivot .
# 3) Now when we are moving from left to right when we get any element which is less than 
#    pivot swap it  at place where we have Swapped last element i.e. at INDEX i+1
# 4) At last we have sorted all the element which are less than pivot .
# 5) Now place pivot where it belongs

from getArray import generateRandomArray

def partition(array,start,last):
	# store last element at pivot 
	pivot=array[last]

	# as initially now swap happen set lastSwapIndex -1
	lastSwapIndex=start-1
	moveIndex=start

	while moveIndex<last:
		
		# check if current element is less than pivot and if less then move it to left 
		if array[moveIndex] < pivot :
			# as we have to move this less than pivot element we have to place it to NEXT to 
			# previous swap - previous less than element
			lastSwapIndex += 1
			tmp = array[moveIndex]
			array[moveIndex]=array[lastSwapIndex]
			array[lastSwapIndex]=tmp

		# move to right by one step	
		moveIndex+=1

	# now we have to place pivot element to position next to lastSwapIndex 
	tmp = array[lastSwapIndex+1]
	array[lastSwapIndex+1]=pivot
	array[last]=tmp
	# array

	return lastSwapIndex+1 	

def quick_sort(array,start,end):
	
	# pivot=partition(array,start,end)
	# print(pivot)
	if start<end:
		pivot=partition(array,start,end)
		quick_sort(array,start,pivot-1)
		quick_sort(array,pivot+1,end)

if __name__ == '__main__':
	array=generateRandomArray(7)
	print("Before Sort : ",array)
	quick_sort(array,0,len(array)-1)
	print("After Sort  : ",array)