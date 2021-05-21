# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head

        return head
h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h1.next = h2
h2.next = h3
h3.next = h4
h4.next = None
b = Solution()
h1 = b.oddEvenList(h1)
while h1:
    print(h1.val)
    h1 = h1.next