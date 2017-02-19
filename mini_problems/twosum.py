

class TwoSum(object):
	def __init__(self,lookup={}):
		self.lookup=lookup
	
	def add(self,value):
		if self.lookup.get(value) is  None:
			self.lookup.update({value:self.find(value)})
		#print self.lookup
			
			
	def find(self,value):
		flag=False
		for key,val in self.lookup.iteritems():
			diff=value-key
			if self.lookup.get(diff) is not None:
				flag=True
		return flag

def main():
	obj=TwoSum()
	obj.add(1)
	obj.add(3) 
	obj.add(5)
	print obj.find(4)
	print obj.find(7)
	
if __name__=='__main__':
	main()