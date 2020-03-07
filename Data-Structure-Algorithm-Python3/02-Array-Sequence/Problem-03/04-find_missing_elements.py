def find_missing_elements(arr1,arr2):
	result=0
	print(arr1+arr2)
	# Perform an XOR between the number int the arrays 
	print()
	for num in arr1+arr2:
		result^=num 
		# print(result)

	print(result)

find_missing_elements([1,2,3,4,5,6,7],[3,7,2,1,4,6])		