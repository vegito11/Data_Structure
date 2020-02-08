# Convert to Lowercase Character
def getLower(char):
	if ord(char)>=65 and ord(char)<=90:
		to_num=ord(char)+26+7-1
		print(to_num)
		# return unichr(to_num)
		return chr(to_num)
	return char	

# Convert to Uppercase Character
def getUpper(char):
	if ord(char)>=97 and ord(char)<=122:
		to_num=ord(char)-26-7+1
		print(to_num)
		# return unichr(to_num)
		return chr(to_num)
	return char	

# check if all character are matched 
def checkBalance(chars):
	sum=0
	for i in chars:
		sum+=i
	
	if sum ==0 :
		return True
	
	return False
#=============================================================
def anagram_check(str1,str2):
	
	chars=[0]*25
	# print(chars)

	for i in str1:
		# if space came ignore it 
		if i==' ': continue

		index=ord(getLower(i))-97
		chars[index]+=1	
	
	# print(chars)
	
	for i in str2:
		
		# if space came ignore it 
		if i==' ': continue

		index=ord(getLower(i))-97
		chars[index]-=1	

		if chars[index] < 0 :
			return False
	
	# print(chars)
	
	return checkBalance(chars)

# result = anagram_check("d o g  ","god")
# print(result)

result = anagram_check("public relations","crap built on lies")
print(result)

result = anagram_check("clint eastwood","old west action")
print(result)


# print(getLower('c'))
# print(getLower('C'))
# print(getUpper('c'))
# print(getUpper('C'))