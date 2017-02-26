def stringSimilarity(str,str2,length):
	n=len(str2)
	print 'n: ',n
	if n==0:
		print '1: ',length
		return length
	else:
		count=0
		for i in str:
			if i == str2[count]:
				length+=1
			else:
				break
		str2=str2[1:]
		print length
		print str2
		stringSimilarity(str,str2,length)
		
def main():
	str='ababaa'
	str2=str[1:]
	len=stringSimilarity(str,str2,0)
	print len
	
if __name__=='__main__':
	main()
	

	