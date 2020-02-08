def unique_character_in_string(str1):

	seen = set()

	for char in str1:

		if char in seen:
			print(False)
			return
		else:
			seen.add(char)	
	
	print(True)
unique_character_in_string("striin1")	
unique_character_in_string("string1")	