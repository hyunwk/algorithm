def bin(n,k): #nCk구하기
	if (k> n//2) : 
		k = n - k
	B = [0] * (k+1)
	B[0] = 1
	for i in range(1, n+1):
		j = min(i, k)
		while( j > 0 ):
			B[j] = B[j] + B[j-1]
			print("j = ",j,"  B[j] =", B[j])
			j=j-1
	return B[k]

print(bin(7,3))


































