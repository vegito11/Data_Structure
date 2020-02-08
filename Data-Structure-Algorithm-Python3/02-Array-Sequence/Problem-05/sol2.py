def sentence_reversal(str1):
	result = str1.split()[::-1]
	print(result)
	result = " ".join(result)
	print(result)
		
sentence_reversal("  This  is the best   ")	