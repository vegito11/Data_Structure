def string_compression(str1):
	length = len(str1)
	
	if length == 0:
		return ""
	if length == 1:
		return str1+"1"
		
	cnt=1
	index = 1
	result=""
	
	while index < length:
		
		#  Check to see if it is the same letter
		if str1[index] == str1[index-1]:
			cnt+=1		
		
		else:
			result+=str1[index-1]+str(cnt)			
			cnt=1		
		index+=1
	result = result+str1[index-1]+str(cnt)
	print(result)

string_compression("AAAABBBBCCCCCDDEEEE")
string_compression("AAAABBBBCCCCCDDEEEED")
string_compression("ABDDEabcbbaae")