def array_pair_sum(array,sum):
	print("-"*25,sum,"-"*25)
	for ele1 in array:
		# if element is greater than skip this element
		if ele1 > sum: continue

		for ele2 in array:
			if ele1+ele2 == sum:
				print([ele1,ele2])

	# return False
	print('-'*53)

array_pair_sum([1,3,6,8],6)	