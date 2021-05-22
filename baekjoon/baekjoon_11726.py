N = int(input())
res = [1, 1, 0]
for i in range(2,N + 1):
    res[i%3] = (res[(i-1)%3] + res[(i-2)%3]) % 10007
print(res[N % 3])
