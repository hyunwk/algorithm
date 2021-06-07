import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    stack = []
    flag = True 
    for c in s:
        if c in "([":
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                flag = False
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                flag = False
                break
    if flag and len(stack) == 0:
        print("yes")
    else:
        print("no")
