import sys
sys.setrecursionlimit(10**5)
def dfs(x, y):
    if x<0 or y<0 or x>=n or y>=m or not graph[x][y]:
        return False
    else:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for  _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] =1
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)
