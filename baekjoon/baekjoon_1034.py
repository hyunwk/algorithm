import sys
N, M = map(int, input().split())
lamp = [sys.stdin.readline() for _ in range(N)]
K = int(input())

dct = {i:amp.count(i) for i in lamp} 
same = 0
for key, v in dct.items():
    zero_cnt = key.count('0')
    if zero_cnt % 2 == K % 2 and zero_cnt <= K:
        if same <= v:
            same = v
print(same)


