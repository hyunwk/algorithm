import sys
In = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, In().split()))
sum_lst = [0] * (n+1)
print()
for i in range(1,n+1):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]

for i in range(m):
    i, j = map(int, In().split())
    print(sum_lst[j] - sum_lst[i-1])
