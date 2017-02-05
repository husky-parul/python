def countingSort(a,m,n):
	'''
	create countArr to count the number of times the numbers m-n occurs in the 
	given array a. initially all position in countArr is assigned 0
	'''
	countArr=[]
	for i in range (m,n+1):
		
		countArr.append(0)
		
	'''
	count the number of times the numbers m-n occurs in the 
	given array a. assign the  position in countArr 
	'''
	
	for i in range(m,n+1):
		for j in range(len(a)):
			if a[j]==i:
				countArr[i]+=1
	
	'''
	find the end index of the positions in the given array a and assign then to countArr
	'''
	
	for i in range(m,n+1):
		if i==m:
			pass
		else:
			countArr[i]=countArr[i-1]+countArr[i]
			
	
	start=0
	end=0
	for i in range(m,n+1):
		if countArr[i]==0:
			pass
		else:
			start=end
			end=countArr[i]
			for j in range(start,end):
				a[j]=i
	
	print a
	
#countingSort([1,4,1,2,7,5,2],0,9)
		
		