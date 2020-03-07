def string_compression(str1):
	if len(str1) == 1:
		return str1+"1"
	
	prev = str1[0]
	cnt=0
	result=''
	for char in str1:
		
		# if repeat increase count
		if char in prev:
			cnt+=1
		
		# if new character is discover add prev char in result
		else:
			result+=prev+str(cnt)
			prev=char
			cnt=1		
	
	print(result+prev+str(cnt))	

string_compression("AAAABBBBCCCCCDDEEEE")
string_compression("AAAABBBBCCCCCDDEEEED")
string_compression("ABDDEabcbbaae")