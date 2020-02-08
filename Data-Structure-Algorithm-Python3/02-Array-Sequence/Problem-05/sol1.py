def sentence_reversal(str1):
	result = str1.split()
	result.reverse()
	result = " ".join(result)
	print(result)
		
sentence_reversal("  This  is the best   ")	