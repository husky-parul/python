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
'''	
print maxSubarraySum([-2,-3,4,-1,-2,1])
print maxSubarraySum([-2,3,2,-1])
print maxSubarraySum([-1, 4, -2, 5, -5, 2, -20, 6])
print maxSubarraySum([-10, -4, -2, -5, -5, -1, -20, -6])
print maxSubarraySum([1,-3,2,-5,7,6,-1,-4,11,-23])
print ('-------------------------------------------------')

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
'''
print maxSubarraySumKadane_([-2,-3,4,-1,-2,1])
print maxSubarraySumKadane_([-2,3,2,-1])
print maxSubarraySumKadane_([-1, 4, -2, 5, -5, 2, -20, 6])
print maxSubarraySumKadane_([-10, -4, -2, -5, -5, -1, -20, -6])
print maxSubarraySumKadane_([1,-3,2,-5,7,6,-1,-4,11,-23])
'''
'''
Given an array of n positive integers and a positive integer s, find the minimal length
of a subarray of which the sum gte s. If there isnt one, return 0 instead.
'''
def minSubarraySum(l,k):
	n=len(l)
	min_length=n+1
	start=end=cur_sum=0
	while end<n :
		while end<n and cur_sum<=k:
			print 'end: ',end
			print 'cur_sum: ',cur_sum
			cur_sum+=l[end]
			print 'cur_sum: ',cur_sum
			end+=1
			print 'end: ',end
		while cur_sum>k and start<n:
			if end-start < min_length:
				min_length=end-start
				print 'min_lenght: ',min_length
			print 'start: ',start
			print 'cur_sum: ',cur_sum
			cur_sum-=l[start]
			print 'cur_sum: ',cur_sum
			start+=1
	return min_length
	
#print minSubarraySum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250],280)

'''
Given a sorted array, remove the duplicates in place such that each element appear
only once and return the new length. Do not allocate extra space for another array,
you must do this in place with constant memory.
For example, given input array A = [1,1,2], your function should return length = 2,
and A is now [1,2].
'''

def removeDupFromSortedArray(l):
	i=0
	j=1
	n=len(l)-1
	last=float('-inf')
	while j<n:
		if l[i]==l[j]:
			j+=1
			
		else:
			
			i+=1
			l[i],l[j]=l[j],l[i]
			j+=1
			last=i
	
	i =0
	count=n-last
	
	while i<count:
		l.pop()
		i+=1
	return l
	
#print removeDupFromSortedArray([1,1,1,1,2,2,3,3,3,3])

'''
Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?
For example, given sorted array A = [1,1,1,2,2,3], your function should return length
= 5, and A is now [1,1,2,2,3].
So this problem also requires in-place array manipulation.
'''
def dupTwice(l):
	prev=l[0]
	flag=False
	count=0
	o=1
	for i in range(len(l)):
		cur=l[i]
		if cur==prev:
			if not flag:
				l[o]=cur
				flag=True
				o+=1
				continue
			else:
				count+=1
		else:
			prev=cur
			l[o]=cur
			o+=1
			flag=False
	num_of_elements=len(l)-count+1
	return l[:num_of_elements]
				
#print dupTwice([1,1,1,2,2,2,2,3,3])		

def dupTwice_(A):
	if len(A)<=2:
		return A
	cur=2
	pre=1
	n=len(A)
	while cur<n:
		if A[cur]==A[pre] and A[cur]==A[pre-1]:
			cur+=1
		else:
			pre+=1
			A[pre]=A[cur]
			cur+=1
			
	return A[:pre+1]

#print dupTwice_([1,1,1,2,2,3,3])

def removeElements(l,val):
	i=0
	j=1
	n=len(l)-1
	while j	<=n:
		if l[i]==val and l[j]!=l[i]:
			if l[j]==val:
				j+=1
			else:
				l[i],l[j]=l[j],l[i]
				j+=1
				i+=1
		else:
			i+=1
			j+=1
			
	return l, i
print 	removeElements([1,2,1,3,5,2,1],2)
		


		
			
	
	
	
	
		

