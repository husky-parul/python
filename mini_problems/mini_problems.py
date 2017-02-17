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
	steps=0
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
	print count, steps
			
		
		
		
	
	
	
wordLadder('hit','cog',["hot","dot","dog","lot","log"])
#twoSumUsingHT([-1,0,1,2,-1,-4],0)
						
#isomorphic('paper','title')
#rotate([1,2,3,4,5,6,7],3)