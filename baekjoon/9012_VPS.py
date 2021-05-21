import sys

def check(s):
    cnt = 0
    for _ in range(len(s)):
        if cnt < 0:
            return "NO"
        c = s.pop()
        if c == ')':
            cnt += 1
        else:
            cnt -= 1
    if cnt:
        return "NO"
    return "YES"

for _ in range(int(input())):
    s = list(sys.stdin.readline().rstrip())
    print(check(s)) 
