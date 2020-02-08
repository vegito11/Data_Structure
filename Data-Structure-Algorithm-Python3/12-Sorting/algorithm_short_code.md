1) Bubble Sort : 

	for ind2 in range(arr_len-round-1):		
		if arr[ind2] > arr[ind2+1]:
			swap(arr,ind2,ind2+1)
_______________________________________________________________________________________	

2) Selection Sort : 
	
	for round in range(arr_len):		
		for ind2 in range(round+1,arr_len):			
			if type=="asc" and arr[round] > arr[ind2]:
				swap(arr,ind2,round)
_______________________________________________________________________________________	

3) Insertion Sort :  
	
	mark first element as sorted

	for each unsorted element X

	  'extract' the element X

	  for j = lastSortedIndex down to 0

	    if current element j > X

	      move sorted element to the right by 1

	    break loop and insert X here
_______________________________________________________________________________________	