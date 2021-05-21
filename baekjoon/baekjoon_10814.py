import sys
In = sys.stdin.readline
lst = [list(In().split()) for n in range(int(input()))]

for s in sorted(lst, key = lambda x: int(x[0])):
    print(s[0], s[1])
