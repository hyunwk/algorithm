# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = node = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            node.next = ListNode(val)
            node = node.next
        return root.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(3)

b = Solution()
a = b.addTwoNumbers(list1, list2)
while a is not None:
    print(a.val)
    a = a.next

