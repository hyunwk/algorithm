import sys
lst = [0 for n in range(0, 20)]

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip().split()
    if "add" == s[0]:
        lst[int(s[1]) - 1] = 1
    elif "remove" == s[0]:
        lst[int(s[1]) -1] = 0
    elif "check" == s[0]:
        print(1 if lst[int(s[1]) - 1] else 0)
    elif "toggle" == s[0]:
        if lst[int(s[1]) - 1]:
            lst[int(s[1])-1] = 0
        else:
            lst[int(s[1])-1] = 1
    elif "all" == s[0]:
        lst = [n for n in range(1, 21)]
    elif "empty":
        lst = [0] * 20
