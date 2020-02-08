def reverseString(str1):
	
	# if last character return that last characer 
	if len(str1)==1:
		return str1
	
	# new string and new string will exclude current letter/first
	# letter and it at last of string 87
	return reverseString(str1[1:])+str1[0]
	# return str1[0]+reverseString(str1[1:])

str1="I am Vegito"
str1="12345678"
print(reverseString(str1))