'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
'''

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        lt=len(s)
        if lt<=1 or s=='':
            return s
        
        max=1
        dp=[[False for x in range(lt)] for x in range(lt)]
        
       
        longest=None
        for l in range(lt):
        	for i in range(lt-l):
        		j=i+l
        		if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
        			dp[i][j]=True
        			if j-i+1>max:
        				max=j-i+1
        				longest=s[i:j+1]
        	
        if longest==None:
        	longest=s[0]
        return longest

print longestPalindrome('bbc')