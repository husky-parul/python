from math import ceil

def heapify(a, size, root):
	largest=root
	l=2*root+1
	r=2*root+2

	#check if left child is bigger than root
	if(l<size  and a[l]>a[largest]):
		largest=l
		
	#check if right child is bigger than root
	if(r<size  and a[r]>a[largest]):
		largest=r
		
	if(largest!=root):
		a[root], a[largest]=a[largest], a[root]
		heapify(a,size,largest)
		
def heapSort(a):
	size=len(a)
	r=(int(ceil(size/2)))-1
	#print r
	for i in range(r,-1, -1):
		heapify(a,size,i)
		
	
	for i in range(size-1,0, -1):
		a[0],a[i]=a[i],a[0]
		heapify(a,i,0)
		
	return a
		
print heapSort([4,10,3,5,1,1,13])
	
	