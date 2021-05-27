import sys
N = int(input())
M = int(input())
s = sys.stdin.readline()
i = cnt = ans= 0
while i < M - 2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            ans += 1
        i += 2
    else:
        cnt = 0
        i += 1
print(ans)
