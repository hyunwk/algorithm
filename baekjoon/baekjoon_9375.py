import sys
In = sys.stdin.readline

for _ in range(int(input())):
    dct = {}
    for _ in range(int(input())):
        name, sort = In().split()
        if dct.get(sort):
            dct[sort] += 1
        else:
            dct[sort] = 1
    ans = 1
    for v in dct.values():
        ans *= v + 1
    print(ans - 1)
