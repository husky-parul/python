'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine
if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" 
and "([)]" are not.
'''

def balancedParan(str):
	lookup={'(':')','[':']','{':'}'}
	stack=[]
	flag=False
	if len(str)==0:
		flag=True
	for i in str:
		if i in ['(','[','{']:
			stack.append(i)
		elif i in [')',']','}']:
			if len(stack)==0:
				print 'Unbalanced: '
				flag=False
				return flag
			else:
				e=stack.pop()
				if lookup.get(e)!=i:
					print 'Unbalanced'
					flag=False
					return flag
				else:
					flag=True
	
	return flag
	
print balancedParan('([)]')
				
	