import sys

def check(x, y, charset):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 1and lines[x+i][y+j] != charset:
                cnt += 1
            if (i+j) % 2 == 0 and lines[x+i][y+j] == charset:
                cnt += 1
    return cnt

N, M = map(int, input().split())
lines = []
cnt = 2500
for i in range(N):
    lines.append(sys.stdin.readline())
for i in range(N-7):
    for j in range(M-7):
        cnt = min(cnt, check(i, j, "B"))
        cnt = min(cnt, check(i, j, "W"))
print(cnt)
