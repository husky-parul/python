'''
Longest Valid Parentheses
Given a string containing just the characters ( and ), find the length of the longest
valid (well-formed) parentheses substring.

For ((), the longest valid parentheses substring is (), which has length = 2.
Another example is )()()) where the longest valid parentheses substring is ()() 
which has length = 4.
'''
def longestValidParan(str):
	lookup={'(':')','[':']','{':'}'}
	stack=[]
	flag=False
	length=0
	max_length=float('-inf')
	if len(str)==0:
		flag=True
		
	for i in str:
		if i in ['(','[','{']:
			stack.append(i)
		elif i in [')',']','}']:
			if len(stack)==0:
				max_length=max(max_length,length)
				flag=False
				length=0
			else:
				e=stack.pop()
				if lookup.get(e)!=i:
					if flag:
						flag=False
						length=0
				else:
					flag=True
					length+=2
					max_length=max(max_length,length)
	
	return max_length
	
print longestValidParan('))()))(())')
				