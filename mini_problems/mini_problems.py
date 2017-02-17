#Rotate an array of n elements to the right by k steps.
#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is 
#rotated to [5,6,7,1,2,3,4]

def rotate(arr,k):
	n=len(arr)
	print n
	first=arr[n-k:] ##all elements from that positon and after
	last=arr[:n-k] ##[1,2,3,4]  first n-k elements
	print first
	print last
	print first+last
	


# Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic
# if the characters in s can be replaced to get t. For example,"egg" and "add" are 
# isomorphic, "foo" and "bar" are not.

def isomorphic(s1,s2):
	lookups1={}
	if len(s1)!= len(s2):
		return 'no'
	count=0
	for i in s1:
		if lookups1.get(i) !=None:
			j,val=lookups1.get(i)
			lookups1.update({i:(j,val+1)})
		else:
			lookups1.update({i:(s2[count],1)})
		count+=1
	print lookups1
	lookups2={}
	count=0
	for i in s2:
		if lookups2.get(i) !=None:
			j,val=lookups2.get(i)
			lookups2.update({i:(j,val+1)})
		else:
			lookups2.update({i:(s1[count],1)})
		count+=1	
	print lookups2
	for key,val in lookups1.iteritems():
		
		val2=lookups2.get(val[0])
		print val, val2, val2[1] , val[1]
		if val2[1]!=val[1]:
			print 'not isomorphic'
			return
	print 'isomorphic'
	
#Given an array of integers, find two numbers such that they add up to a specific target
#number.

def twoSumUsingHT(l,sum):
	lookup={}
	result=set()
	for n in l:
		lookup.update({n:sum-n})
	for n in l:
		if lookup.get(n) in l:
			result.update([(n,sum-n)])
	for n in result:
		print n
	

twoSumUsingHT([-1,0,1,2,-1,-4],0)
						
#isomorphic('paper','title')
#rotate([1,2,3,4,5,6,7],3)