import sys
n = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
cnt = 0
result = []

def bfs(i, j):
    global cnt
    if i<0 or j<0 or i>=n or j>=n or not graph[i][j]:
        return False
    else:    
        cnt += 1
        graph[i][j] = 0
        bfs(i-1,j)
        bfs(i+1,j)
        bfs(i,j-1)
        bfs(i,j+1)
        return True
        
for i in range(n):
    for j in range(n):
        cnt = 0
        if bfs(i,j):
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i)
