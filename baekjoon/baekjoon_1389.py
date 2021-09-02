from collections import deque
import sys
sys.setrecursionlimit(20000)
def dfs(v, n):
    visited = [0] * (n+1)
    visited[v] = True
    queue = deque()
    queue.append((v, 0))
    total = 0
    while queue:
        v, cnt = queue.popleft()
        total += cnt 
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, cnt+1))
    return total

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

result = []
for v in range(1, n+1):
    result.append(dfs(v, n))
print(result.index(min(result)) + 1)
