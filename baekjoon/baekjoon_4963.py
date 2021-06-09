import sys
sys.setrecursionlimit(10**6)
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y):
    graph[x][y] = 0
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0<=nx<h and 0<=ny<w and graph[nx][ny] ==1:
            dfs(nx,ny)
                
while True:
    w, h = map(int, input().split())
    if w == h== 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)
