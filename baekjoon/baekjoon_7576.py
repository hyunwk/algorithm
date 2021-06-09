import sys
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
flag = True
queue = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))

while queue:
    i, j = queue.popleft()
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0<=x<m and 0<=y<n and graph[x][y] == 0:
            queue.append((x,y))
            graph[x][y] = graph[i][j] + 1 
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            flag = False
if flag:
    print(max(map(max, graph)) - 1)
else:
    print(-1)
