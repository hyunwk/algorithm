import collections


class MyStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        #value = self.stack[-1]
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print(obj.top())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())
