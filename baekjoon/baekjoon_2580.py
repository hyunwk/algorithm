import sys
def backtrack(k):
    if k == blank_cnt+1:
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=' ')
            print()
        sys.exit()

    y, x = blank[k-1]
    for i in range(1, 10):
        if not used_y[y][i] and not used_x[x][i] and not used_box[(y-1)//3*3+(x-1)//3][i]:
            used_y[y][i] = used_x[x][i] = used_box[(y-1)//3*3+(x-1)//3][i] = 1
            graph[y-1][x-1] = i
            backtrack(k+1)
            used_y[y][i] = used_x[x][i] = used_box[(y-1)//3*3+(x-1)//3][i] = 0
            graph[y-1][x-1] = 0
            
graph = [list(map(int, input().split())) for _ in range(9)]
used_x = [[0] * 10 for _ in range(10)]
used_y = [[0] * 10 for _ in range(10)]
used_box = [[0] * 10 for _ in range(10)]
blank = []
for i in range(1,10):
    for j in range(1,10):
        if graph[i-1][j-1] == 0:
            blank.append([i,j])
        else:
            used_y[i][graph[i-1][j-1]] = 1
            used_x[j][graph[i-1][j-1]] = 1
            used_box[(i-1)//3*3+(j-1)//3][graph[i-1][j-1]] = 1
blank_cnt = len(blank)
backtrack(1)
