# Import Stack from Previous Folder 
from Stack import Stack

def balance_para(str1):
	str1=str1.replace(" ","")
	print("=-"*20)
	st = Stack()
	opening = ['{','[','(']
	closing = ['}',']',')']
	matches = [('(',')'),('[',']'),('{','}'),]
	
	# print(str1)

	for bracket in str1:

		# print(bracket)
		# if bracket in '{  (  [' push in Stack
		if bracket in opening:
			st.push(bracket)
		
		# if bracket is closing pop from stack and compare it Previous bracket
		else:	
			# Get Previous Item from Stack should be opening
			prev=st.pop()
			
			pair = (prev,bracket)
										
			if pair in matches:
				continue
			else:
				print("Required ",bracket," for closing")
				return False
	
	if st.isEmpty():
		return True

	print(" Not enough closing brackets")	
	return False	


print(balance_para("[({{} }  )]  "))
print(balance_para("[}"))
print(balance_para("[[["))
print(balance_para("[()()[{}]]"))
print(balance_para("[()()[{}]])"))

