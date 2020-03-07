# 5=1+2+3+4+5=15
def findSum(num):
	
	# base condition when reach to last 1 break
	if num==1:
		return 1
	
	return num+findSum(num-1)


sum = findSum(10)
print(sum)