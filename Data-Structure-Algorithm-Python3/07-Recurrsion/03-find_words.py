# 
def word_split(phrase,list_of_words,output=None):
	
	# initiallize the output variable
	if output is None :
		output=[]

	for word in list_of_words :
		
		# if string start with this word add it in word Array
		if phrase.startswith(word):
			output.append(word)

			# new phrase will remove thise matched word from start 	
			phrase=phrase[len(word):]	
			return word_split(phrase,list_of_words,output)

	return output	

result = word_split("themanran",['clown','man','ran'])
print(result)
result = word_split("ilovedogsJohn",['i','am','a','dog','lover','love','john'])
print(result)
