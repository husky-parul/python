import sys
'''
I was asked this during a Google Interview. We are given a string consisting of letters- 
G,L,R. - which is the instruction a robot follows
G- goes forward by one step.
L-turn left.
R- turn right.
The string runs itself infinite times. We need to tell if there exists a circle with a 
radius, r( r can be any real number), such that the robot never leaves the circle.
'''
def executeCommands(command):
	initial_face='N'
	right_lookup={'N':'E','S':'W','E':'S','W':'N'}
	left_lookup={'N':'W','S':'E','E':'N','W':'S'}
	count=0
	pos=(0,0,'N')
	i_pos=(0,0,'N')
	initial_dir=pos[2]
	if len(command)==1 and command=='G':
		return 'NO'
		
	while count<=3:
		for s in command:
			if s =='G':
				pos=moveForward(pos)
			elif s=='R':
				pos=(pos[0],pos[1],right_lookup.get(pos[2]))
			else:
				pos=(pos[0],pos[1],left_lookup.get(pos[2]))
			#print 'pos: ',pos
		
		count+=1
		
	if i_pos==pos:
		return 'YES'
	else:
		return 'NO'	
			
def moveForward(pos):
	if pos[2]=='N':
		return (pos[0],pos[1]+1,pos[2])
	elif pos[2]=='S':
		return (pos[0],pos[1]-1,pos[2])
	elif pos[2]=='E':
		return (pos[0]+1,pos[1],pos[2])
	else:
		return (pos[0]-1,pos[1],pos[2])
		
	
	
def main():
	numElements=int(raw_input())
	commands=[]
	for i in range(0,numElements):
		#print i
		commands.append(raw_input())
	#print '1: ', commands
	#print 'length: ',len(commands)
	result=[]
	for c in range(len(commands)):
		#print '2: ',commands[c]
		result.append(executeCommands(commands[c]))
	print result

if __name__=='__main__':
	main()
	
	
	
	