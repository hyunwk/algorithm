class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        num = int(str(abs(x))[::-1])
        if num > 2**31:
            return 0
        return sign * num
