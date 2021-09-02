import sys
n = int(input())
target_x, target_y = map(int, input().split())
m = int(input())
members = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int ,input().split())
    members[x].append(y)
    members[y].append(x)

q = []
cnt = 0
q.append((target_x, 0))
flag = True
while q and flag:
    x, cnt = q.pop()
    for member in members[x]:
        if member == target_y:
            flag = False 
            print(cnt + 1)
        if not visited[member]:
            visited[member] = 1
            q.append((member, cnt+1))
if flag:
    print(-1)
