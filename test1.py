import sys
In = sys.stdin.readline
n = int(In())
lst = []
res = [0] * (n ** 2)
for i in range(n):
    lst.append(list(map(int, In().split())))

for i in range(n):
    part = (n ** 2) // (i+1)
    for j in range(16):
        res[j] += lst[i][j // part]
print(max(res))
