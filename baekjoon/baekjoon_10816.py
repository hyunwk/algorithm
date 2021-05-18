import sys
In = sys.stdin.readline
dct = {}
N = int(input())
for item in In().split():
    if item not in dct:
        dct[item] = 1
    else:
        dct[item] += 1
M = int(input())
for item in In().split():
    if item in dct:
        print(dct[item], end=' ')
    else:
        print(0, end=' ')
