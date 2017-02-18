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
	
					
regularExpressionMatching('aab','c*a*b')	
		
#wildcardMatching('xaylmz','x?y*z')
#klargestElements([3,2,1,5,6,4],2)
#medianTwoSortedArr([1, 12, 15, 26, 38],[2, 13, 17, 30, 45])	
#wordLadder('hit','cog',["hot","dot","dog","lot","log"])
#twoSumUsingHT([-1,0,1,2,-1,-4],0)
						
#isomorphic('paper','title')
#rotate([1,2,3,4,5,6,7],3)