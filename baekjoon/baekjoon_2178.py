import sys
from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]
queue = deque()
queue.append((0,0))

while queue:
    i, j = queue.popleft()
    if i==n-1 and j==m-1:
        print(visited[n-1][m-1])
        break

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = visited[i][j] + 1
                queue.append([nx, ny])
