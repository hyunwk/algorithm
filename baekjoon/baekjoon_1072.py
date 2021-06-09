from math import floor
x, y = map(int, input().split())
z = floor(100 * y/x) 
low, high = 0, 1000000000
if x == y or z >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        now = floor(100 * (y+mid)/(x+mid))
        if now > z:
            high = mid - 1
        else:
            low = mid + 1
    print(high + 1)
