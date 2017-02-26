
#["gab", "cat", "bag", "alpha"] => [["gab", "bag"], ["bag", "gab"]]
#["gab", "cat", "bag", "alpha", "nurses", "race", "car", "run"] => [["gab", "bag"], ["bag", "gab"], ["race", "car"], ["nurses", "run"]]
def findPallindrome(l):
    result=[]
    flag=False
    for i in l:
    	for j in l:
    		if i==j:
    			continue
    		else:
    			index_i=0
    			index_j=len(j)-1
    			while index_j > 0 and index_i < len(i):
    				if i[index_i]==j[index_j]:
    					flag=True
    					index_i+=1
    					index_j-=1
    				else:
    					flag=False
    					break
    			if flag:
    				result.append((i,j))
    return result

def main():
    l=["gab", "bag", "alpha", "nurses", "race", "car", "run"]
    #l=["gab", "bag", "alpha"]
    r=findPallindrome(l)
    print r
    
if __name__=='__main__':
    main()
    
             
                    
                    
                        
                    
                
                    

