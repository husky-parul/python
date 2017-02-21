def closetSum(A,target):
	min=float('inf')
	A.sort()
	for i in range(len(A)-2):
		j=i+1
		k=len(A)-1
		while(j<k):
			sum=A[i]+A[j]+A[k]
			diff=abs(sum-target)
			if diff==0:
				return sum
			if diff<min:
				diff=min
				result=sum
			if sum<target:
				j+=1
			else:
				k-=1
	return result
	

print closetSum([-4,-1,1,2],1)			