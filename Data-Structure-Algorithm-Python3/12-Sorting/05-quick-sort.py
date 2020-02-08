# Properties : 
# 1) Not stable
# 2) O(lg(n)) extra space (see discussion)
# 3) O(n2) time, but typically O(n·lg(n)) time
# 4) Not adaptive

from getArray import generateRandomArray

def partition(array,start,last):
	# store first element at pivot 
	pivot=array[start]

	leftIndex=start+1
	rightIndex=last

	while leftIndex<rightIndex:
		
		# it will break when ''element'' at left index is greater than pivot 
		while leftIndex<rightIndex and array[leftIndex]<pivot:
			# leftIndex element is less than pivot hence go to rightIndex by one step
			leftIndex+=1

		# it will break when ''element'' at rightIndex index is less than pivot 
		while array[rightIndex]>pivot:
			# rightIndex element is less than pivot hence go to leftIndex by one step
			rightIndex-=1
		
		if rightIndex < leftIndex: break 	
		else:	
			# swap the element at leftIndex with element at rightIndex 
			# bcz LeftIndex > pivot and right < pivot
			tmp=array[leftIndex]
			array[leftIndex]=array[rightIndex]
			array[rightIndex]=tmp

	# now rightIndex will be where element is less than pivot 
	# so place this element at 0th Position 		
	array[start]=array[rightIndex]
	# now place pivot at rightIndex(where we encotered element less than pivot) 
	array[rightIndex]=pivot

	return rightIndex 	

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

"""
	1) Choose start index element as pivot element
	2) Now go from From LEFT=Start+1 go to right until we reach to Element which is Greater than PIVOT
	3) Now go from From RIGHT=Last go to left until we reach to Element which is Less than PIVOT
	4) Now Swap this element LeftIndex which element greater than Pivot with rightIndex smaller than 
	   pivot element 
	5) Note: In while condtion of right we have not included right > left bcz at last swap we have to 
	         find out element which are going to swap with pivot . That is pivot position
	6) At last we move rightIndex to point where we will get element less than pivot so It will be 
	   pivot position as leftIndex must have completed its movement


"""