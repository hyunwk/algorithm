import sys
In = sys.stdin.readline

def deq_command(s:str):
    if "push_front" == s[:s.find(' ')]:
        deq.insert(0, s[s.find(' ') + 1:])
    elif "push_back" == s[:s.find(' ')]:
        deq.append(s[s.find(' ') + 1:])
    elif "pop_front" == s:
        print(deq.pop(0) if len(deq) else -1)
    elif "pop_back" == s:
        print(deq.pop() if len(deq) else -1)
    elif "size" == s:
        print(len(deq))
    elif "empty" == s:
        print(0 if len(deq) else 1)
    elif "front" == s:
        print(deq[0] if len(deq) else -1)
    elif "back" == s:
        print(deq[-1] if len(deq) else -1)

deq = []
for _ in range(int(input())):
    deq_command(In().rstrip())
