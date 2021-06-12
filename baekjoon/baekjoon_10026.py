import sys
from collections import deque
def bfs(i,j,graph):
    c = graph[i][j]
    graph[i][j] = 0
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            tx = x + dx[k]
            ty = y + dy[k]
            if 0<=tx<n and 0<=ty<m and graph[tx][ty] == c:
                graph[tx][ty] = 0
                q.append((tx,ty))

n = int(input())

rgb = [list(map(int, sys.stdin.readline().rstrip().replace('R','1').replace('G','2').replace('B','3'))) for _ in range(n)]
m = len(rgb[0])
rb = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        rgb[i][j] = int(rgb[i][j])
        if rgb[i][j] == 2:
            rb[i][j] = 1
        else:
            rb[i][j] = rgb[i][j]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
rgb_cnt = 0
rb_cnt = 0
for i in range(n):
    for j in range(m):
        if rgb[i][j]:
            bfs(i,j,rgb)
            rgb_cnt+=1
for i in range(n):
    for j in range(m):
        if rb[i][j]:
            bfs(i,j,rb)
            rb_cnt+=1
print(rgb_cnt, rb_cnt)

