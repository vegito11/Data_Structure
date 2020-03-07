# Big O(n)
list1 = [10,3,4,60,80]
list2 = [110,23,44,560,180,54,12]

def linear(list):
	for index,item in enumerate(list, start=1):
		print("comparison : ",index)
	print("-"*40)
linear(list1)	
linear(list2)	