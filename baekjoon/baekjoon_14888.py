def backtrack(i,k, p, m, t, d ):
    if k == n:
        global max_res
        global min_res
        max_res = max(max_res, i)
        min_res = min(min_res, i)
        return
    if p:
        backtrack(i + nbrs[k], k+1,p-1,m,t,d)
    if m:
        backtrack(i - nbrs[k], k+1,p, m-1, t, d)
    if t:
        backtrack(i * nbrs[k], k+1, p, m, t-1, d)
    if d:
        if i<0:
            backtrack(-(-i // nbrs[k]), k+1, p, m, t, d-1)
        else:
            backtrack(i // nbrs[k], k+1,p, m, t, d-1)

n = int(input())
nbrs = list(map(int, input().split()))
ops = list(map(int, input().split()))
max_res = -100000001
min_res = 100000001
backtrack(nbrs[0],1,ops[0],ops[1],ops[2],ops[3])
print(max_res)
print(min_res)
