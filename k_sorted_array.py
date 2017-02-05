from math import ceil
from mergesort import merge, mergeSort

'''
Sort a nearly sorted (or K sorted) array
Given an array of n elements, where each element is at most k away from its target
position, devise an algorithm that sorts in O(n) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, 
can be at indexes 5, 6, 7, 8, 9 in the given array.

First sort the first group of k elements Arr(0 to k).
Then, sort the second group of k elements (positions k+1 through 2k) and merge with the
sorted first group. so on and so forth....

Since there are n/k groups, and each sort and merge are constant time, we obtain a running time
of O(n).

merge-sort take theta(nlog n)

 theta((n/k)k log k + (n/k)k) = theta(n log k). considering k very less than n logk will be very 
 very less than n. Hence O(n)
 
'''


def ksorted(a,k):
	size=len(a)
	count=0
	upto=(size-(size-(count+1)))+1
	groups=int((ceil(size/k)))
	

	mergedArr=[]
	for i in range(1,groups+1):
		temp=[]
		for j in range(count,upto):
			temp.append(a[j])
		
		mergedArr=merge(mergedArr, mergeSort(temp))
		count+=2
		upto=(size-(size-(count+1)))+1
		
	print mergedArr
	

		
ksorted([4,3,1,13,10,5],2)		
		

		
	