import sys
In = sys.stdin.readline

def stack_command(s):
    if s[:4] == "push":
        stack.append(list(s[s.find('h')+2:]))
    
    elif s == "pop":
        if len(stack):
            print(''.join(stack[-1]))
            del stack[-1]
        else:
            print(-1)

    elif s == "size":
        print(len(stack))

    elif s == "empty":
        if len(stack):
            print(0)
        else:
            print(1)

    elif s == "top":
        if len(stack):
            print(''.join(stack[-1]))
        else:
            print(-1)
            
stack = []
for i in range(int(input())):
    stack_command(In().rstrip())
