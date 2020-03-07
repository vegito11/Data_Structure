# Big O(n^2)
list1 = [10,3,4,60,80]
list2 = [110,23,44,560,180,54,12]

def quad(list):
	k=0
	for i in list:
		for j in list:			
			print("{}  {}".format(i,j))
			k+=1
	print("-"*40)
	print(" Ran %d Times"%(k))

quad(list1)	