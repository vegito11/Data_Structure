def anagram_check(str1,str2):
	str1 = str1.replace(" ","").lower()
	str2 = str2.replace(" ","").lower()
	# print(sorted(str1))
	# print(sorted(str2))

	return sorted(str1) == sorted(str2)

result = anagram_check("public relations","crap built on lies")
print(result)

result = anagram_check("clint eastwood","old west action")
print(result)

str1 ="public relaERtions"

