# Import Stack from Previous Folder 
from Stack import Stack

def balance_para(str1):
	str1=str1.replace(" ","")
	print("=-"*20)
	
	st = []
	
	opening = ['{','[','(']
	
	matches = [('(',')'),('[',']'),('{','}'),]
		

	for bracket in str1:

		# print(bracket)
		# if bracket in '{  (  [' push in Stack
		if bracket in opening:
			st.append(bracket)
		
		# if bracket is closing pop from stack and compare it Previous bracket
		else:	
			# Get Previous Item from Stack should be opening
			if len(st) == 0:
				return False
			prev=st.pop()
			
			pair = (prev,bracket)
										
			if pair in matches:
				continue
			else:
				print("Required ",bracket," for closing")
				return False
	
	# If not empty
	if len(st)==0:
		return True

	print(" Not enough closing brackets")	
	return False	


print(balance_para("[({{} }  )]  "))
print(balance_para("[}"))
print(balance_para("[[["))
print(balance_para("[()()[{}]]"))
print(balance_para("[()()[{}]])"))

