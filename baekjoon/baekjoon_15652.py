def backtrack(k):
    if k == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n+1):
        if k > 0:
            if arr[k-1] > i:
                continue
        arr[k] = i
        backtrack(k + 1)
                
n, m = map(int, input().split())
arr = [0] * m
backtrack(0)
