import sys
from collections import deque
n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_cnt = 0
di = [1,-1,0,0]
dj = [0,0,1,-1]
def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        i, j = q.popleft()
        for cnt in range(4):
            ni = i + di[cnt]
            nj = j + dj[cnt]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni,nj))

for k in range(2,max(map(max,graph))):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= k:
                visited[i][j] = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
                bfs(i,j)
    if cnt == 0:
        break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
