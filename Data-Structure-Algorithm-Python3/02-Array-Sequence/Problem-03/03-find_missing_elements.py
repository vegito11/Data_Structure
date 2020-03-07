import collections

def find_missing_elements(arr1,arr2):

	# If key not there initiallize it to zero 
	d = collections.defaultdict(int)

	for num in arr2
		d[num]+=1

	for num in arr1:
		if d[num]==0:
			print(num)
		else:
			print(-1)		

find_missing_elements([1,2,3,4,5,6,7],[3,7,2,1,4,6])