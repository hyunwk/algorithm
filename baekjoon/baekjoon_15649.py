def back(k):
    if k == m:
        for i in arr:
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1):
        if not isused[i]:
            isused[i] = 1
            arr[k] = i
            back(k+1)
            isused[i] = 0

n, m = map(int ,input().split())
arr = [0] * m
isused = [0] * (n+1)
back(0)
