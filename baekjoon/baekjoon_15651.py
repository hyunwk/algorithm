def bak(k):
    if k == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n+1):
        arr[k] = i
        bak(k+1)
n, m = map(int, input().split())
arr = [0] * m
bak(0)
