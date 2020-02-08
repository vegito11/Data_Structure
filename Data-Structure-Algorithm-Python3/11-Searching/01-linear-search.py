# 1) If Item is Present     :   O(1)   O(n)   O(n/2)
# 2) If Item is not Present :   O(n)   O(n)   O(n)

def printResult(result):
	if result[0]:print(" Element found at location ",result[1])
	else: print(" !!!! Element  is not Present in Array!!! ")	

def sequenctial_search(arr,search_ele):
	index=0
	for element in arr:
		if search_ele==element:
			return True,index
		index+=1	
	return False,None

persons=["Vegito","Omkar","Neymar","Leo","Sterling","Salah"]

result=sequenctial_search(persons,"Omkar")
printResult(result)
result=sequenctial_search(persons,"omkar")
printResult(result)
result=sequenctial_search(persons,"Ethun")
printResult(result)

