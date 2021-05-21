import sys
In = sys.stdin.readline

dct_k = {}
dct_v = {}
N, M = map(int, input().split())

for i in range(1, N + 1):
    s = In().rstrip()
    if s not in dct_k:
        dct_k[i] = s
        dct_v[s] = i 

for _ in range(M):
    s = In().rstrip()
    if s.isdigit():
        print(dct_k[int(s)])
    else:
        print(dct_v[s])
