# 3145=3+1+4+5=13
def findSum(num):
	# if we reach divide num till its first digit 3/10
	if num==0:
		return 0

	# last digit of number
	dig=num%10
	return dig+findSum(num//10)


sum = findSum(3145)
print(sum)