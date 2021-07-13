def backtrack(k):
    global cnt
    if k == n:
        cnt += 1
        return 
    for i in range(1, n+1):
        if isused1[i] or isused2[n+k-i] or isused3[k+i]:
            continue
        isused1[i] = 1
        isused2[n+k-i] = 1
        isused3[k+i] = 1
        backtrack(k + 1)
        isused1[i] = 0 
        isused2[n+k-i] = 0
        isused3[k+i] = 0

n = int(input())
isused1= [0] * (n*2)
isused2= [0] * (n*2)
isused3= [0] * (n*2)
cnt = 0
backtrack(0)
print(cnt)
