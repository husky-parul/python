def  maxStep(n, k):
    DP=[]
    DP.append(0)
    for i in range(1,n+1):
        DP.append(0)
    #print DP
    for i in range(1,n+1):
        if DP[i-1]+i==k:
            DP[i]=DP[i-1]
            continue
        else:
            val1=DP[i-1]+0+i+1
            #print val1
            val2=DP[i-1]+i+i+1
            #print val2
            if val1==k:
                val1=0
            if val2==k:
                val2=0
            if val1>val2:
                DP[i]=DP[i-1]
            else:
                DP[i]=DP[i-1]+i
    return DP[n]
    
def main():
	n=raw_input()
	k=raw_input()
	r=maxStep(int(n),int(k))
	print r

if __name__=='__main__':
	main()
	