# 1) If Item is Present     :   O(1)   O(logn)   O(logn)
# 2) If Item is not Present :   O(logn)   O(logn)   O(logn)

def printResult(result):
	if result[0]:print(" Element found at location ",result[1])
	else: print(" !!!! Element  is not Present in Array!!! ")	

def binary_search(arr,search_ele):
	found=False
	start=0
	end=len(arr)
	mid=(start+end)//2

	while start<end:
		# if mid is the search element then return it   ===========
		if arr[mid]==search_ele:
			return True,mid

		# search element is greater than mid then search toward Right side ---->	
		if search_ele>arr[mid]:
			start=mid+1
		
		# search element is greater than mid then search toward Right side <----
		else:
			end=mid-1
		mid=(start+end)//2	

	return False,None	

#    0    1   2    3    4    5    6    7   8
#   [10, 20, 30 , 45 , 52 , 63 , 87 , 89 , 99 ] => 9/2=4

#    0    1   2    3    4    5    6    7   8    9
#   [10, 20, 30 , 45 , 52 , 63 , 87 , 89 , 93 , 99 ] 10/2 = 5


if __name__ == '__main__':
	age=[10,20,30,45,52,63,87,99,104]
	result=binary_search(age,30)
	printResult(result)
	result=binary_search(age,40)
	printResult(result)


