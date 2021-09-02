lst = list(input())
stack = []
amount = 0
def is_open(c):
    if c in ('(', '[')

def is_close(c):
    if c in (')', ']')

for i in range(len(lst)):
    if is_open(lst[i]):
        stack.push(lst[i])
    elif is_close(lst[i]):
        try:
            if lst[i] == stack.pop():
                if lst[i] == ')':
                    amount += 2
                elif lst[i] == ']':
                    amount += 3

        except:
            print(0)
            break



