from mergesort import mergeSort
'''
Given an array A[] and a number x, check for pair in A[] with sum as x

'''

def findPairsWithSumX(a,sum):
	start=0
	end=len(a)-1
	pairs=()
	a=(mergeSort(a))
	a.reverse()
	
	while start!=end:
		if a[start]+a[end]>sum:
			end-=1
			
		elif a[start]+a[end]<sum:
			start+=1
			
		elif a[start]+a[end]==sum:
			pairs+=((a[start],a[end]),)
			start+=1
			end-=1
			
			
	print pairs
	return pairs
	
findPairsWithSumX([1,4,1,2,7,5,2],6)