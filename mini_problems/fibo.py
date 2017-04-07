def fibo(n):
	fib={0:0,1:1}
	for i in range(2,n+1):
		n1=fib.get(i-1)
		n2=fib.get(i-2)
		fib.update({i:n1+n2})
	print fib
	return fib.get(n)

print fibo(5)
			
		
