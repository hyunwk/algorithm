import sys, heapq

def queue_command(n):
    if n == 0 and q:
        print(heapq.heappop(q)) 
    elif n == 0:
        print(0)
    else:
        heapq.heappush(q, n)

q = []
for _ in range(int(input())):
    queue_command(int(sys.stdin.readline()))
