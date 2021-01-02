d = [0] * 100

def pibo(n):
	print(n)
	if 1 == n or 2 == n:
		return 1
	if 0 != d[n]:
		return d[n]
	d[n] = pibo(n-1) + pibo(n-2)
	return d[n]
	

pibo(6)
