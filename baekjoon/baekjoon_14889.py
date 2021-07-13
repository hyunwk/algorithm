import sys
def backtrack(idx, k):
    if k == n//2:
        global res
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if isused[i] and isused[j]:
                    start += graph[i][j]
                elif not isused[i] and not isused[j]:
                    link += graph[i][j]
        res = min(res, abs(start - link))
        return
    for i in range(idx, n):
        if not isused[i]:
            isused[i] = 1
            backtrack(i+1, k+1)
            isused[i] = 0
        
n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
isused = [0] * (n)
res = 100000000
backtrack(0, 0)
print(res)
