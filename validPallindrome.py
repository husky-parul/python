def validPallindrome(str):
	str=str.lower()
	s=str.replace(' ','')
	j=len(s)-1
	flag=False
	i=0
	
	while (i<j):
		
		
		if s[i].isalnum() and s[j].isalnum():
			if s[i] == s[j]:
				flag=True
				i+=1
				j-=1
			elif flag==False:
				break
			else:
				flag=False
		elif not s[i].isalnum():
			i+=1
		elif not s[j].isalnum():
			j-=1
	
			
	if flag:
		print 'Pallindrome'
	else:
		print 'Not pallindrome'
		

validPallindrome('Red rum, sir, is murder')
			
			
			
		