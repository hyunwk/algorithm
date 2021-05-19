import sys
In = sys.stdin.readline

def queue_command(s: str):
    if s[:4] == "push":
        lst.append(s[s.find(' ')+1:])
    elif s == "pop":
        print(lst.pop(0) if len(lst) else -1)
    elif s == "size":
        print(len(lst))
    elif s == "empty":
        print(0 if len(lst) else 1)
    elif s == "front":
        print(lst[0] if len(lst) else -1)
    elif s == "back":
        print(lst[-1] if len(lst) else -1)
        
lst = []
for _ in range(int(input())):
    queue_command(In().rstrip())
    
