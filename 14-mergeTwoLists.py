# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        curr = head

        while  l1 != None and l2 != None :
            if l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            else :
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        if l1 != None:
            curr.next = l1
        else:
            curr.next = l2
        return head.next


    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
           l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1

a = ListNode(2)
b = ListNode(3)
c = ListNode(1)
d = ListNode(4)
a.next = b
c.next = d

k = Solution()
a = k.mergeTwoLists2(a, c)
while a is not None:
    print(a.val)
    a = a.next
