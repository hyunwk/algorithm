class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode, ListNode
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(None))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(None))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.head.right.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

obj = MyCircularDeque(6)
param_1 = obj.insertFront(4)
print(param_1)
param_2 = obj.insertLast(3)
print(param_2)
param_3 = obj.deleteFront()
print(param_3)
param_4 = obj.deleteLast()
print(param_4)
param_5 = obj.getFront()
print(param_5)
param_6 = obj.getRear()
print(param_6)
param_7 = obj.isEmpty()
print(param_7)
param_8 = obj.isFull()
print(param_8)
