import sys
In = sys.stdin.readline
n, m = map(int, input().split())
dct={}
for _ in range(n):
    url, pw = In().rstrip().split()
    dct[url] = pw
for _ in range(m):
    print(dct[In().rstrip()])
