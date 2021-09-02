from collections import deque
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]
for _ in range(int(input())):
    length = int(input())
    graph = [[0] * length for _ in range(length)]
    queue = deque()
    i, j = map(int ,input().split())
    queue.append((i,j))
    target_x, target_y = map(int, input().split())

    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            print(graph[x][y])
            break
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<length and 0<=ny<length and graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
