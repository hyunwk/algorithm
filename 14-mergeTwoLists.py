# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
           l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

a = ListNode(2)
b = ListNode(3)
c = ListNode(1)
d = ListNode(4)
a.next = b
c.next = d

k = Solution()
a = k.mergeTwoLists(a, c)
while a is not None:
    print(a.val)
    a = a.next
