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
	
rotate([1,2,3,4,5,6,7],3)