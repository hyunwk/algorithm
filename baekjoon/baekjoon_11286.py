import sys
import heapq as h
lst = []
for i in range(int(input())):
    n = int(sys.stdin.readline())
    if n:
        h.heappush(lst, (abs(n), n))
    else:
        if lst:
            print(h.heappop(lst)[1])
        else:
            print(0)
