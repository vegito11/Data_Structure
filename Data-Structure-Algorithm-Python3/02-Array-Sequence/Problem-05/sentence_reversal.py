def sentence_reversal(str1):
	
	words = []
	length = len(str1)
	i = length-1 
	result=""
	while i >= 0 :		
		
		if str1[i] is not ' ' :			
			word_end = i
			while str1[i] is not ' ':
				i-=1
			# print(word_end,i)
			# print(str1[i:word_end+1])
			result+=str1[i:word_end+1]
		i-=1	
	print(result)	

sentence_reversal("  This  is the best   ")	