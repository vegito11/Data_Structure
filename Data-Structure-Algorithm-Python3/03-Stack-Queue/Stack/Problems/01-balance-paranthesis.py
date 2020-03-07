# Import Stack from Previous Folder 
from Stack import Stack

def balance_para(str1):
	print("=-"*20)
	st = Stack()
	opening = ['{','[','(']
	closing = ['}',']',')']
	str1=str1.replace(" ","")
	
	# print(str1)

	for bracket in str1:

		# print(bracket)
		# if bracket in '{  (  [' push in Stack
		if bracket in opening:
			st.push(bracket)
		
		# if bracket is closing pop from stack and compare it Previous bracket
		else:	
			# Get Previous Item from Stack 
			prev=st.pop()
			# print("Prev= ",prev)
			
			# get corresponding opening bracket 
			# get index of } ] ) so that we will get corresponding opening
			close=closing.index(bracket)
			if opening[close] == prev:
				continue
			else:
				print("Required ",opening[close]," for closing")
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

