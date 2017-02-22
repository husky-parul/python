'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function 
search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. 
You may assume that n > m.
'''

def searchString(str1,str2):
	n=len(str1)
	m=len(str2)
	matched=False
	result=[]
	i=j=start=0
	while i<n+1:
		#print i , n
		if j==m and matched:
			result.append(start)
			j=0
			matched=False
			continue
		if i==n:
			if matched:
				result.append(start)
			break
		if str1[i]==str2[j]:
			if j==0:
				start=i
				matched=True
			i+=1
			j+=1
		else:
			matched=False
			i+=1
			j=0
	return result if len(result)!=0 else -1
	
print searchString('AABAACAADAABAABA','AABA')
	