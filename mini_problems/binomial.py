import sys
def binomial(n,m):
	# number of ways to choose m things out of n possiilities
	n=int(n)
	m=int(m)
	dp=[[0 for x in range(n+1)]for x in range(m+1)]
	print dp
	for i in range(n+1):
		dp[0][i]=1
	for j in range(m+1):
		dp[j][0]=0
	dp[0][0]=1
	print '------------',dp 
	for i in range(1,m+1):
		for j in range(1,i+1):
			dp[j][i]=dp[j-1][i-1]+dp[j][i-1]
	print dp
	return dp[m][n]

#n=raw_input()
#m=raw_input()
print binomial(5,4)
