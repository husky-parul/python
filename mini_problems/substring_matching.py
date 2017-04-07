def substring_matching(p,t):
	opt=[]
	k=0
	i,j=0,0
	while i<len(t) and j<len(p) :
		print i,j
		if t[i]==p[j]:
			opt.append(i)
			i+=1
			j+=1
			k+=1
		else:
			i+=1
	return  opt

print substring_matching('uten','you hat eng')
	
