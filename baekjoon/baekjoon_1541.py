import sys
s = [sum(map(int, n.split('+'))) for n in sys.stdin.readline().rstrip().split('-')]

print(s[0] - sum(s[1:]))
