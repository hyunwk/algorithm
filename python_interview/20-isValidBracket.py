class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for char in s:
            if char in table:
                stack.append(char)
            elif not stack or char != table[stack.pop()]:
                return False
        return len(stack) == 0


s = "()]"
b = Solution()
print(b.isValid(s))
