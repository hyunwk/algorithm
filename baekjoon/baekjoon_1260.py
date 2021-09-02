from collections import deque

def dfs(v):
    visited[v] = True
    print(v,end=' ')

    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 0 

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = 0

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0] * (n+1)
dfs(v)
print()
bfs(v)
