from  math import ceil
import sys

def mergeSort(a):
	n=len(a)
	l1=[]
	l2=[]
	
	if n==1:
		return a
	
	for x in range(0,n/2):
		l1.append(a[x])
		
	for x in range(int(ceil(n/2)),n):
		l2.append(a[x])
	
	l1=mergeSort(l1)
	l2=mergeSort(l2)
	
	return merge(l1,l2)
	
def merge(l1,l2):
	c=[]
	
	while l1 and l2:
		if l1[0]>l2[0]:
			c.append(l1[0])
			l1.remove(l1[0])
		else:
			c.append(l2[0])
			l2.remove(l2[0])
			
	while  len(l1)!=0:
		c.append(l1[0])
		l1.remove(l1[0])
		
	while len(l2)!=0:
		c.append(l2[0])
		l2.remove(l2[0])
		
	return c
	
	

print 'sorted array: ', mergeSort([14,33,27,10,35,19,42,44])
	