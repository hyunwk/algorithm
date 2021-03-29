from typing import List
class Solution:
    def reverseString1(self, s: List[str]) -> None:
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString2(self, s: List[str]) -> None:
        s.reverse()
s =  ["s", "d"]
f = Solution()

for i in s:
    print(i, end=' ')
f.reverseString1(s)
for i in s:
    print(i, end=' ')
print()
f.reverseString2(s)
for i in s:
    print(i, end=' ')
