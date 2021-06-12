import sys
from collections import deque
def bfs(i,j):
    cnt = 0
    queue = deque()
    queue.append((i,j))
    while queue:
        y, x = queue.popleft()
        cnt+=1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=nx<n and 0<=ny<m and not square[ny][nx]:
                square[ny][nx] = 1
                queue.append((ny, nx))
    return cnt

m, n, k = map(int, input().split())
square = [[0] * n for _ in range(m)]
result = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if not square[i][j]:
                square[i][j] = 1
for i in range(m):
    for j in range(n):
        if not square[i][j]:
            square[i][j] = 1 
            result.append(bfs(i,j))
print(len(result))
result.sort()
for i in result:
    print(i, end=' ')
