def minimumPathSum(grid):
	m=len(grid)
	n=len(grid[0])
	
	dp=[[0 for x in range(n)]for x in range(m)]
	dp[0][0]=grid[0][0]
	
	#initialize top
	for x in range(1,n):
		dp[0][x]=dp[0][x-1]+grid[0][x]
	for j in range(1,m):
        	dp[j][0] = dp[j-1][0] + grid[j][0]
    
 
   	 #fill up the dp table
    	for i in range(1,m):
    		for j in range(1,n):
    			if dp[i-1][j] > dp[i][j-1]:
                		dp[i][j] = dp[i][j-1] + grid[i][j]
            		else:
                		dp[i][j] = dp[i-1][j] + grid[i][j]
            
    	return dp[m-1][n-1]
    	
print minimumPathSum([[0]])
	
		
