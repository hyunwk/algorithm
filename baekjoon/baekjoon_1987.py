import sys
r, c = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0,-1, 1]
max_len = 0
def dfs(y,x,ans):
    global max_len
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<r and 0<=nx<c and graph[ny][nx] not in ans:
            max_len = max(max_len, len(ans)+1)
            dfs(ny, nx, ans + graph[ny][nx])

            
dfs(0,0,'')
print(max_len-1)
