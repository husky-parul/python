'''
queue in python
'''
#>>> from collections import deque
#>>> d=deque([1,2,3])
#>>> d.append(7)
#>>> print d
#deque([1, 2, 3, 7])
#>>> d.popleft()
#1
#>>> print d
#deque([2, 3, 7])

'''
stack implementaion in python

stack=[100,200,300]
print stack #[100, 200, 300]
stack.append(900)
print stack #[100, 200, 300, 900]
print stack.pop() #900

'''



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
		
#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
#Find all unique triplets in the array which gives the sum of zero.
#Note: Elements in a triplet (a,b,c) must be in non-descending order.
#The solution set must not contain duplicate triplets.

#Given two words (start and end), and a dictionary, find the length of shortest 
#transformation sequence from start to end, such that only one letter can be changed at a 
#time and each intermediate word must exist in the dictionary. For example, given:
#start = "hit"
#end = "cog"
#dict = ["hot","dot","dog","lot","log"]
import string
from collections import deque
def wordLadder(start,end,dict):
	node=(start,start)
	frontier=deque([node])
	explored=[]
	path=()
	parent={start:None}
	while len(frontier)!=0:
		word,path=frontier.popleft()
		explored.append(word)
		for s in word:
			for w in string.lowercase[:26]:
				next_word=word.replace(s,w) 
				if next_word==end:
					parent.update({next_word:word})
					break
				if next_word in dict and next_word not in explored and next_word not in frontier:
					path=path+','+next_word
					node=(next_word,path)
					frontier.append(node)
					parent.update({next_word:word})
					
					
	val=parent.get(end)
	count=0
	while val is not None:
		val=parent.get(val)
		count+=1
	print count
			
		
'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the 
two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
import math

def medianTwoSortedArr(a,b):
	#print '-----------------'
	x=int(((len(a)-1)/2))
	y=int(((len(b)-1)/2))
	
	#print x,y
	#print a[x],b[y]
	if len(a)==len(b)==2:
		first=max(a[0],b[0])
		last=min(a[1],b[1])
		#print first , last
		print float((first+last)/2)
		return
	elif a[x]>b[y]:
		c=b[y:]
		d=a[:x+1]
		#print 'b: ', c
		#print 'a: ',d
		medianTwoSortedArr(d,c)
	elif a[x]<b[y]:
		c=b[:y+1]
		d=a[x:]
		#print 'b: ', c
		#print 'a: ',d
		medianTwoSortedArr(d,c)
	
	
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element
in the sorted order, not the kth distinct element.
For example, given [3,2,1,5,6,4] and k = 2, return 5.
'''	
from heapq import heappush,heappop,heapify
def klargestElements(a,k):
	heap=[]
	poped=[]
	ordered=[]
	for x in a:
		heappush(heap,x)
		if len(heap)>k:
			poped.append(heappop(heap))
	while heap:
			ordered.append(heappop(heap))
	print ordered[0]
	
'''
Implement wildcard pattern matching with support for '?' and '*'.
'''
def wildcardMatching(text,pattern):
	t=len(text)
	p=len(pattern)
	
	# Creates a list containing t lists, each of p items, all set to False
	T=[[False for x in range(p+1)]for y in range(t+1)]
	
	#base conditions: when text is empty and pattern is empty
	if t==0 and p==0:
		T[0][0]=True
		return
	
	#when pattern is * and text is empty
	if t==0 and p==1 and pattern[0]=='*':
		T[0][1]=True
		return
	
	#when pattern is empty but text is not
	if p==0 and t!=0:
		for i in range(t+1):
			T[i][0]=False
			return
	
	#initializing  T[0][] 
	T[0][0]=True
	for i in range(1,t+1):
		T[i][0]=False
	
	#initializing  T[][0] 
	for j in range(1,p+1):
		if pattern[0]=='*':
			T[0][1]=True
		else:
			T[0][j]=False
	
	#recurrence
	it=0
	for i in range(1,t+1):
		pt=0
		for j in range(1,p+1):
			if  text[it]==pattern[pt] or pattern[pt]=='?':
				T[i][j]=T[i-1][j-1]
			elif pattern[pt]=='*':
				T[i][j]=T[i-1][j] or T[i][j-1]
			else:
				T[i][j]=False
			pt+=1
		it+=1
	
	if T[t][p]==True:
		print 'Matches'
	else:
		print 'Not Matches'

'''
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'''	
def regularExpressionMatching(text,pattern):
	t=len(text)
	p=len(pattern)
	T=[[False for j in range(p+1)]for i in range(t+1)]
	
	# when text is null and pattern in null
	if t==p==0:
		print 'Matches'
		return
		
	# if pattern is null but text has at least one character
	
	T[0][0]=True
	for x in range(1,t+1):
		T[x][0]=False
		
	if pattern[0]=='*':
		print 'No Matching'
		return
		
	T[0][0]=True
	#if pattern has at least one element but text is empty
	
	for x in range(1,p+1):
		if pattern[x-1]=='*':
			T[0][x]=T[0][x-2]
	
	#all other cases
	it=0
	for x in range(1,t+1):
		pt=0
		for y in range(1,p+1):
			if text[it]==pattern[pt] or pattern[pt]=='.':
		 		T[x][y]=T[x-1][y-1]
		 	elif pattern[pt]=='*':
		 		if T[x][y-2] == True:
		 			T[x][y]=True
		 			break
		 		elif text[it]==pattern[pt-1] or pattern[pt-1]=='.':
		 			T[x][y]=T[x-1][y]
			else:
				T[x][y]=False
			pt+=1
		it+=1	
	print T
	if T[t][p]==True:
		print 'Matches'
	else:
		print 'Not matching'
		
'''
Given a collection of intervals, merge all overlapping intervals.
For example, Given [1,3],[2,6],[8,10],[15,18]
return [1,6],[8,10],[15,18].
'''

def mergeIntervals(l):
	from math import ceil,floor
	from collections import deque
	
	def mergeSort(l):
		n=int(ceil(len(l)/2))
		
		
		if len(l)==1:
			return l
		l1=l[:n]
		l2=l[n:]
		#print n
		#print l1
		#print l2
		#print '_______________'
		l1=mergeSort(l1)
		l2=mergeSort(l2)
		
		
		return merge(l1,l2)
		
	def merge(l1,l2):
		c=[]
		#print 'l1: ', l1
		#print 'l2: ',l2
		while l1 and l2:
			e1=l1[0]
			e2=l2[0]
			if e1[0] < e2[0]:
				c.append(e1)
				l1.remove(e1)
			elif e1[0] > e2[0]:
				c.append(e2)
				l2.remove(e2)
			elif e1[0]==e2[0]:
				if e1[1]<=e2[1]:
					c.append(e1)
					l1.remove(e1)
				else:
					c.append(e2)
					l2.remove(e2)
					
		while l1:
			c.append(l1[0])
			l1.remove(l1[0])
		while len(l2)!=0:
			c.append(l2[0])
			l2.remove(l2[0])
		
		return c
		
	#sl= mergeSort([[2,3],[1,10],[3,6],[15,18],[2,13],[0,0]])
	
	def fuse(sl):
		new=[]
		fuse_possible=False
		last_compare=(None,None)
		for i in range(len(sl)-1):
			first=sl[i]
			last=sl[i+1]
			largest=0
			smallest=0
			if first[1] < last[1] and first[1] > last[0]:
				largest=last[1]
				smallest=first[0]
				fuse_possible=True
				
			elif first[1] > last[1] and last[0] > first[0]:
				largest=first[1]
				smallest=first[0]
				fuse_possible=True
				
			else:
				fuse_possible=False
				new.append(first)
				print 'in else:first ',first, 'new: ',new
			
			compare_with=(smallest,largest)
			
			if fuse_possible:
				sl[i+1]=sl[i]=compare_with
				if last_compare!=compare_with:
					new.append(compare_with)
				
			last_compare=compare_with
			
		if sl[len(sl)-1]!=last_compare:
			new.append(sl[len(sl)-1])
			
		print 'fused: ',sl
		print 'new: ',new
		count=0
		count=len(sl)-1
		q=[]
		
		while count!=0:
			if sl[count]!=sl[count-1]:
				q.append(sl.pop())
			else:
				sl.pop()
			count-=1
			
		
		print 'final: ',q
		
	
	sl= mergeSort(l)
	print 'sorted : ',sl
	fuse(sl)
	
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique
combinations in C where the candidate numbers sums to T. Each number in C may only be used
ONCE in the combination.

Note:
1) All numbers (including target) will be positive integers.
2) Elements in a combination must be in non-descending order. 
3) The solution set must not contain duplicate combinations.
'''
			
def combinationSum(l,sum):
	lookup={}
	result=[]
	prev=-1
	for i in range(len(l)):
		if prev!=l[i]:
			diff=sum-l[i]
			if lookup.get(diff) is not None:
				result.append(l[i])
				result.append(diff)
			else:
				lookup.update({l[i]:diff})
		prev=l[i]
	result.sort()
	print result
	
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0
Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. 
The solution set must not contain duplicate triplets.
For example, given array S = {-1 0 1 2 -1 -4},
A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''
def threeSum(A,sum):
	result=()
	A.sort()
	for i in range(len(A)):
		if i==0 or A[i]>A[i-1]:  #checking duplicates at i index
			j=i+1
			k=len(A)-1
			while (j<k):
				current_sum=A[i]+A[j]+A[k]
				if current_sum ==0:
					result+=((A[i],A[j],A[k]),)
					j+=1
					k-=1
					while j<k and A[j]==A[j-1]: # checking duplicates
						j+=1
					while j<k and A[k]==A[k+1]: # checking duplicates
						k-=1
				elif current_sum < 0:
					j+=1
				else:
					k-=1
	return result
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that 
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order.
The solution set must not contain duplicate quadruplets.
For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

A solution set is:
(-1,  0, 0, 1)
(-2, -1, 1, 2)
(-2,  0, 0, 2)
'''
def ksum(A,sum,x):
	result=()
	A.sort()
	for i in range(len(A)-3):
		for j in range(i+1,len(A)-2):
				k=j+1
				l=len(A)-1
				while k<l:
					current_sum=A[i]+A[j]+A[k]+A[l]
					if current_sum==sum:
						result+=(A[i],A[j],A[k],A[l]),
						k+=1
						l-=1
						while k<l and A[k]==A[k-1]:
							k+=1
						while k<l and A[l]==A[l+1]:
							l-=1
					elif current_sum<sum:
						k+=1
					else:
						l-=1
	r=set(result)
	return r
			
#print ksum([1, 0, -1, 0, -2, 2],0,0)
#print threeSum([-1,0,1,2,-1,-4],0)
#combinationSum([1,1,2,3,4,5],6)	
#mergeIntervals([[2,3],[1,10],[3,6],[15,18],[2,13]])
#mergeIntervals([[2,3],[1,10],[3,6],[15,18],[2,13],[0,0]])				
#regularExpressionMatching('aab','c*a*b')	
#wildcardMatching('xaylmz','x?y*z')
#klargestElements([3,2,1,5,6,4],2)
#medianTwoSortedArr([1, 12, 15, 26, 38],[2, 13, 17, 30, 45])	
#wordLadder('hit','cog',["hot","dot","dog","lot","log"])
#twoSumUsingHT([-1,0,1,2,-1,-4],0)
#isomorphic('paper','title')
#rotate([1,2,3,4,5,6,7],3)