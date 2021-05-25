import sys
In = sys.stdin.readline
N, M = map(int, In().split())
dct = {}
ans = []
for _ in range(N):
    dct[In().rstrip()] = 1
for _ in range(M):
    s = In().rstrip()
    if dct.get(s):
        ans.append(s)
ans.sort()
print(len(ans))
for name in ans:
    print(name)
