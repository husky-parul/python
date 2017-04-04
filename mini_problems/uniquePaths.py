'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if m==0 or n==0:
            return 0
        if m==1 or n==1:
            return 1
        dp=[[0 for x in range(n)]for x in range(m)]
        #left column
        for i in range(m):
            dp[i][0]=1
        #top row
        for i in range(n):
            dp[0][i]=1
        #populate the table
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]