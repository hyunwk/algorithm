import sys
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for n in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (n+1)
cnt = 0

for v in range(1, n+1):
    if not visited[v]:
        dfs(v)
        cnt += 1
print(cnt)
