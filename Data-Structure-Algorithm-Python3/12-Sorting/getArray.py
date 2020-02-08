import random
def generateRandomArray(size=10):
	arr=[]
	for i in range(size):
		num=random.randint(12,439)
		arr.append(num)
	return arr	

if __name__ == '__main__':
	array=generateRandomArray()
	print(array)