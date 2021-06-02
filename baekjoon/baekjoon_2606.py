from collections import deque
n = int(input())
m = int(input())

lst = [[] for n in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

visited = [0] * (n+1)
visited[1] = True
queue = deque([1])
cnt = 0
while queue:
    v = queue.popleft()
    for i in lst[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            cnt += 1
print(cnt)

