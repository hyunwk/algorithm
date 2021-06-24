import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph =[[] for _ in range(n+1)]
parent_lst = [0] * (n+1) 
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(n, parent):
    parent_lst[n] = parent 
    for i in graph[n]:
        if not parent_lst[i]:
            dfs(i, n)
dfs(1, 0)

for i in range(2, n+1):
    print(parent_lst[i])
