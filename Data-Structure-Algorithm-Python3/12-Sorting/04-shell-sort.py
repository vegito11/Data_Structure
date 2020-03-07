# Properties : 
# 1) Not stable
# 2) O(1) extra space
# 3) O(n^3/2) time complexity  in average case O(n * log n)
# 4) Adaptive: O(n·lg(n)) time when nearly sorted

# Reference : https://www.programiz.com/dsa/shell-sort

from getArray import generateRandomArray

def shell_sort(main_array):
	# 11/2=5
	 gap = len(main_array) // 2
	 while gap > 0:
	 	 # we are interating from 5 to 10
	     for i in range(gap, len(main_array)):
	         # store each element from 5,6,...10th index
	         temp = array[i]

	         # store current index bcz we are going to decreament in while loop 
	         j = i

	         # compare each element to its index-gap element like 5 to 0 , 6 to 1 , 10 to 5
	         # if forward element[temp] is smaller then swap
	         while j >= gap and array[j - gap] > temp:
	             
	         	 # put the smaller element which is (array[j]-left) at the (right-(array[j-gap]))
	             array[j] = array[j - gap]
	             # decrease j by gap steps like 6-5=1 ,
	             j -= gap

	         # put the Temp element at its right position if j is changed by while loop swap will happen    
	         array[j] = temp

	     # decrease gap at each step 5/2=2 , 2//2=1 , 1//2=0
	     gap //= 2


if __name__ == '__main__':
	array=generateRandomArray(11)
	print("Before Sort : ",array)
	shell_sort(array)
	print("After Sort  : ",array)
