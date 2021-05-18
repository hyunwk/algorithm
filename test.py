import sys
In = sys.stdin.readline

n = int(In())
lst = []
for i in range(n):
    lst.append(list(map(int, In().split())))
    if i == 0:
        continue
    for j in range(len(lst[i])):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        elif j == i:
            lst[i][j] += lst[i-1][j-1]
        else:
            lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])
print(max(lst[i])) 
