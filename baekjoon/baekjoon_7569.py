import sys
from collections import deque
m,n,h = map(int, input().split())
graph = []
dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
for i in range(h):
    graph.append([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)])
queue = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                queue.append((k,i,j))

while queue:
    z,y,x = queue.popleft()
    for k in range(6):
        nz = z + dz[k]
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = graph[z][y][x] + 1
            queue.append((nz,ny,nx))
result = -1
for k in graph:
    for i in k:
        if 0 in i:
            print(-1)
            sys.exit()
        result = max(result, max(i))
if result == 1:
    print(0)
else:
    print(result-1)
