# O(n) complexity
def array_pair_sum(array,sum):
	
	print("-"*25,sum,"-"*25)

	# Set for target
	pairs = set()
	seen = set()
	
	for ele1 in array:
		
		# if element is greater than skip this element
		if ele1 > sum: continue
		print("ele1:",ele1)
		target=sum-ele1
		# print(target)

		if target not in seen:
			seen.add(ele1)
		else:	
			print("..")
			pairs.add((min(target,ele1),max(target,ele1)))
		print(seen)	

	print("\n".join(map(str,list(pairs))))

array_pair_sum([1,3,2,2],4)	