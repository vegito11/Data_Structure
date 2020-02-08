def uni_char(s ):
	return len(set(s)) == len(s)

print(uni_char("asdqwAA"))
print(uni_char("asdqwA"))