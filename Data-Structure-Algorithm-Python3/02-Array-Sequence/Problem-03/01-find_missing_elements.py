# problem is if numbers are long ovrflow will be there
import functools
def find_missing_elements(arr1,arr2):
	sum1 = functools.reduce(lambda ele1,ele2:ele1+ele2 , arr1)
	sum2 = functools.reduce(lambda ele1,ele2:ele1+ele2 , arr2)	
	# print(sum1)
	# print(sum2)  
	print(sum1-sum2)
	

find_missing_elements([1,2,3,4,5,6,7],[3,7,2,1,4,6])