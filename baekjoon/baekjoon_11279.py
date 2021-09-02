import heapq, sys
heap = []
for n in map(int, sys.stdin):
    if n:
        heapq.heappush(heap, -n)
    else:
        if heap:
            print(heapq.heappop(heap) * -1)
        else:
            print(0)
