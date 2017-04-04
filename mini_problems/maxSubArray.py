def maxSubArray(A):
	max_sum=A[0]
	sum=A[0]
	for i in range(1,len(A)):
		sum=max(sum+A[i],A[i])
		max_sum=max(max_sum,sum)
	return max_sum
	
print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
