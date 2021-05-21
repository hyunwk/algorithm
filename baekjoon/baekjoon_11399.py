N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
res = 0
for i in range(len(lst)):
    res += (i + 1) * lst[i]
print(res)


