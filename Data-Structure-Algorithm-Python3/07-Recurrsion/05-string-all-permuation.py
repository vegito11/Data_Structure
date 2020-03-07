# *** Itertool library	
# given string return all permutation of that string
# 'abc' = ['abc','acb','bac','bca','cab','cba']
def permutation(phrase,leftIndex,strLength):
	# print("Enter Permutation function ")

	# this will run number of possible permutation times means n!
	if leftIndex==strLength:
		print(phrase)
	else:
		for i in range(leftIndex,strLength):
			# print(i,leftIndex)

			# swap character at index left and i 
			phrase=swapChar(phrase,leftIndex,i)

			# now go to next index char and swap it remember strLength always same
			permutation(phrase,leftIndex+1,strLength)

def swapChar(str1,index1,index2):
	# Use this Bcz TypeError: 'str' object does not support item assignment

	c = list(str1)
	c[index1], c[index2] = c[index2], c[index1]

	return ''.join(c)

phrase="abcd"

# we start permutation from first character(0) till last character(len)
permutation(phrase,0,len(phrase))

"""
1) Base Case : 
	When left==right index 

2) Repeat: 
	a) First 'swap' first character to all possible position 
		ABCD  BACD   CBAD   DBCA 
		0      1       2       3
	
		* above we have used string 'ABCD' and swapped A character 
		  from position 0 to 3 

	b) next in second step swap second character in all possible space 
	   for all above strings ( from that index onward here 1,2,3) 
                 .            .        .
	   **[ We have swapped SECOND char from index 1 to 3]
	
	   ABCD ->  ABCD    |   ACBD   |  ADCB
                 1            2          3 
	             *           *         *
	   BACD ->  BACD    |   BCAD   |  BDCA
              	 1            2          3   

	             *           *         *
	   CBAD ->  CBAD    |   CABD   |  CDAB
              	 1            2          3   

	             *           *         *
	   DBCA ->  DBCA    |   DCBA   |  DACB
              	 1            2          3   
	
	C) now in next step we run it for all 12 string which are above 
	   from index 2 to 3 
		
		[ Swapped THIRD character from 2nd index position till end position ]
				   ^		^
		ABCD ->  ABCD   | ABDC  
		           2         3
				   
				   ^        ^ 	
		ACBD ->  ACBD   | ACDB
		           2         3

		           ^         ^
		ADCB ->  ADCB   |  ADBC
				   2          3  
		____________________________________
	
				   ^		^
		BACD ->  BACD   | BADC  
		           2         3

				   ^	    ^
		BCAD ->  BCAD   | BCDA
		           2         3

		           ^         ^
		BDCA ->  BDCA   |  BDAC
				   2          3  
		____________________________________
	
	D) in this step 3 to 3 . hence breaking condition and we get all the strings
	   - Means we have to start swapping from 3rd index till last index . 
	   - But 3rd index is last index hence we print the string
	   - and we get (number_of_char)! strings

"""