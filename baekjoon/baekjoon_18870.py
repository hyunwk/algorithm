import sys
input()
items = list(map(int, sys.stdin.readline().split()))
dct = {}
for i, v in enumerate(sorted(list(set(items)))):
    dct[v] = i
for i in items:
    print(dct[i], end=' ')
