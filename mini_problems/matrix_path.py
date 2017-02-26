def  count(a):
    import math
    m=len(a)
    n=len(a[0])
    count=[[0 for x in range(n)] for y in range(m)] 
    
    for i in range(m):
        count[i][0]=0
    for i in range(n):
        count[0][i]=0
        
    for i in range(m):
        for j in range(n):
            if a[i][j-1]!=0:
            	count[i][j]+=count[i][j-1]
            if count[i-1][j]!=0:
                count[i][j]+=count[i-1][j]
            print count[i][j]
    result=count[m-1][n-1] %((math.pow(10,9))+7)
    return result
    
    
def paths(r,c,m,n):
	if r==m-1:
		return 1
	if c==n-1:
		return 1
		
	return paths(r,j+1,c,m,n)+path(r+1,c,m,n)
    
def main():
	m=3
	n=4
	a=[[1 for x in range(n)] for y in range(m)]
	print  paths(a)
    
if __name__=='__main__':
	main()
