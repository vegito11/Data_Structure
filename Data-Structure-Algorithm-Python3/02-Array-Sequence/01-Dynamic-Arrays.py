import sys
data = []

for i in range(1,51):
	
	# Number of elements
	length = len(data)

	# Actual Size in Bytes 
	size = sys.getsizeof(data)

	print(f' Length: {length:3d} ; Size in bytes: {size:4d}')

	# increase length by one
	data.append(i)

"""
	 Length:   0 ; Size in bytes:   36
	 Length:   1 ; Size in bytes:   52
	 Length:   2 ; Size in bytes:   52
	 Length:   3 ; Size in bytes:   52
	 Length:   4 ; Size in bytes:   52
	 Length:   5 ; Size in bytes:   68
	 Length:   6 ; Size in bytes:   68
	 Length:   7 ; Size in bytes:   68
	 Length:   8 ; Size in bytes:   68
	 Length:   9 ; Size in bytes:  100
	 Length:  10 ; Size in bytes:  100
	 Length:  11 ; Size in bytes:  100
	 Length:  12 ; Size in bytes:  100
	 Length:  13 ; Size in bytes:  100
	 Length:  14 ; Size in bytes:  100
	 Length:  15 ; Size in bytes:  100
	 Length:  16 ; Size in bytes:  100
	 Length:  17 ; Size in bytes:  136
	 Length:  18 ; Size in bytes:  136
	 Length:  19 ; Size in bytes:  136
	 Length:  20 ; Size in bytes:  136
	 Length:  21 ; Size in bytes:  136
	 Length:  22 ; Size in bytes:  136
	 Length:  23 ; Size in bytes:  136
	 Length:  24 ; Size in bytes:  136
	 Length:  25 ; Size in bytes:  136
	 Length:  26 ; Size in bytes:  176
	 Length:  27 ; Size in bytes:  176
	 Length:  28 ; Size in bytes:  176
	 Length:  29 ; Size in bytes:  176
	 Length:  30 ; Size in bytes:  176
	 Length:  31 ; Size in bytes:  176
	 Length:  32 ; Size in bytes:  176
	 Length:  33 ; Size in bytes:  176
	 Length:  34 ; Size in bytes:  176
	 Length:  35 ; Size in bytes:  176
	 Length:  36 ; Size in bytes:  220
	 Length:  37 ; Size in bytes:  220
	 Length:  38 ; Size in bytes:  220
	 Length:  39 ; Size in bytes:  220
	 Length:  40 ; Size in bytes:  220
	 Length:  41 ; Size in bytes:  220
	 Length:  42 ; Size in bytes:  220
	 Length:  43 ; Size in bytes:  220
	 Length:  44 ; Size in bytes:  220
	 Length:  45 ; Size in bytes:  220
	 Length:  46 ; Size in bytes:  220
	 Length:  47 ; Size in bytes:  268
	 Length:  48 ; Size in bytes:  268
	 Length:  49 ; Size in bytes:  268
	>>> 

"""	