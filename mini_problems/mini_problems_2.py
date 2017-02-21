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
				min=diff
				result=sum
			if sum<target:
				j+=1
			else:
				k-=1
	return result
	
#print closetSum([-4,-1,1,2],1)	

'''
Maximum Subarray Sum
'''

def maxSubarraySum(l):
	#print '----------------'
	n=len(l)
	if n==1:
		return l[0]
	m=n/2
	#print 'l[:m]: ',l[:m]
	#print 'r[m:]: ',l[m:]
	left_arr=maxSubarraySum(l[:m])
	right_arr=maxSubarraySum(l[m:])
	sum=0
	rsum=float('-inf')
	lsum=float('-inf')
	for i in range (m,n):
		sum+=l[i]
		rsum=max(rsum,sum)
	sum=0
	#print 'rsum: ',rsum
	for i in range (m-1,-1,-1):
		sum+=l[i]
		lsum=max(lsum,sum)
	#print 'lsum: ',lsum
	ans=max(right_arr,left_arr)
	#print 'ans: ',ans
	#print 'lsum+rsum: ',lsum+rsum
	return max(ans,lsum+rsum)
	
print maxSubarraySum([-2,-3,4,-1,-2,1])
print maxSubarraySum([-2,3,2,-1])
print maxSubarraySum([-1, 4, -2, 5, -5, 2, -20, 6])
print maxSubarraySum([-10, -4, -2, -5, -5, -1, -20, -6])
print maxSubarraySum([1,-3,2,-5,7,6,-1,-4,11,-23])
print ('-------------------------------------------------')
'''
Maximum Subarray Sum
Does not work for negative numbers
Time complexity O(n)
'''
def maxSubarraySumKadane(l):
	max_so_far=max_ends_here=0
	for i in l:
		max_ends_here=max_ends_here+i
		if max_ends_here<0:
			max_ends_here=0
		if max_so_far<max_ends_here:
			max_so_far=max_ends_here
	return max_so_far

#print maxSubarraySumKadane ([2,-3,4,-1,2,1,5,-3])
#print maxSubarraySumKadane([-2,-3,4,-1,-2,1])
#print maxSubarraySumKadane([-2,3,2,-1])
#print maxSubarraySumKadane ([1,-3,2,1,-1])

'''
Maximum Subarray Sum
Does  work for negative numbers
Time complexity O(n)
'''
def maxSubarraySumKadane_(l):
	max_so_far=max_ends_here=0
	max_val=float('-inf')
	for i in l:
		max_ends_here=max_ends_here+i
		max_val=max(i,max_val)
		if max_ends_here<0:
			max_ends_here=0
		if max_so_far<max_ends_here:
			max_so_far=max_ends_here
	if max_so_far==0:
		return max_val
	else:
		return max_so_far

print maxSubarraySumKadane_([-2,-3,4,-1,-2,1])
print maxSubarraySumKadane_([-2,3,2,-1])
print maxSubarraySumKadane_([-1, 4, -2, 5, -5, 2, -20, 6])
print maxSubarraySumKadane_([-10, -4, -2, -5, -5, -1, -20, -6])
print maxSubarraySumKadane_([1,-3,2,-5,7,6,-1,-4,11,-23])

