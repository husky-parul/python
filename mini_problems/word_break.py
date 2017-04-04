'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

def wordBreak(s, wordDict):
	lt=len(s)
	pos=[-1 for x in range(lt+1)]
	pos[0]=0
	
	for i in range(lt):
		if pos[i]!=-1:
			for j in range(i+1,lt+1):
				sub=s[i:j]
				
				if sub in wordDict:
					pos[j]=i
				
	return pos[len(s)]!=-1
    
print wordBreak('leetcode', ['leet','code'])