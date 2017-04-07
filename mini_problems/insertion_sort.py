def insertion_sort(list):
	print '------------',list
	l=len(list)
	for i in range(l):
		for j in range(0,i):
			if list[i]<list[j]:
				list[i],list[j]=list[j],list[i]
			print list
	return list
print insertion_sort([21,3,5,1,112,0]) 
