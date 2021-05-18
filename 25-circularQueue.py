class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.fr = 0
        self.re = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.fr] is None:
            self.q[self.fr] = value
            self.fr = (self.fr + 1) % self.maxlen
            return True
        else:
            False

    def deQueue(self) -> bool:
        if self.q[self.re] is None:
            return False
        else:
            self.q[self.re] = None
            self.re = (self.re + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.fr] is None else self.q[self.fr]

    def Rear(self) -> int:
        return -1 if self.q[self.re] is None else self.q[self.re]

    def isEmpty(self) -> bool:
       return self.re == self.fr and self.q[self.re] is None

    def isFull(self) -> bool:
        return self.re == self.fr and self.q[self.re] is not None
obj = MyCircularQueue()
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()