from collections import deque
n, k =map(int, input().split())
visited = [0] * (10**5 + 1)
queue = deque()
queue.append(n)
while queue:
    i = queue.popleft()
    if i == k:
        print(visited[i])
        break
    for v in (i-1, i+1, 2*i):
        if 0<=v<=10**5 and not visited[v]:
            visited[v] = visited[i] + 1
            queue.append(v)

