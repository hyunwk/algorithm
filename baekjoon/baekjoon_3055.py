import sys
import copy
from collections import deque
r, c = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

water = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            water.append((i, j))
        if graph[i][j] == 'S':
            graph[i][j] = 0
            q.append((i, j))
        if graph[i][j] == 'D':
            target_y, target_x = i,j

flag = True
while q and flag:

    q_bak = deque(copy.deepcopy(q))
    q = []
    for y, x in q_bak:
        if graph[y][x] == '*':
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny == target_y and nx == target_x:
                graph[ny][nx] = graph[y][x] + 1
                flag = False
                break
             
            if 0<=ny<r and 0<=nx<c and graph[ny][nx] == '.':
                graph[ny][nx] = graph[y][x] + 1 
                q.append((ny, nx))
    if flag:
        water_bak = deque(copy.deepcopy(water))
        water = []
        for y, x in water_bak:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
    
                if 0 <= ny < r and 0 <= nx < c:
                    if graph[ny][nx] != '*' and graph[ny][nx] != 'X' and graph[ny][nx] != 'D' and graph[ny][nx] != 'S':
                        graph[ny][nx] = '*'
                        water.append((ny, nx))
    
if graph[target_y][target_x] == 'D':
    print("KAKTUS")
else:
    print(graph[target_y][target_x])
