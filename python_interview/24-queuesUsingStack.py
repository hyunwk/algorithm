class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []


    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def peek(self) -> int:
        if not self.output:
            while self.input:
               self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
