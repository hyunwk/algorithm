# Definition for singly-linked list.
import collections


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import List

class Solution:
    def isPalindrome1(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None :
            q.append(node.val)
            node = node.next

        while len(q) > 1 :
            if q.pop(0) != q.pop():
                return False
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        q: collections.deque = collections.deque()

        if not head :
            return True

        node = head
        while node is not None :
            q.append(node.val)
            node = node.next

        while len(q) > 1 :
            if q.popleft() != q.pop():
                return False
        return True

    def isPalindrome3(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val :
              rev, slow = rev.next, slow.next
            #slow, rev = slow.next, rev.next
        return not rev


head = [1,2,2,1]
a = ListNode()
b = ListNode()
c = ListNode()
a.val = 1
b.val = 2
c.val = 1
a.next = b
b.next = c
c.next = None

b = Solution()
print(b.isPalindrome1(a))
print(b.isPalindrome2(a))
print(b.isPalindrome3(a))
