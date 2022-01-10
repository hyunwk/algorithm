class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign *= -1;
            s = s[1:]
        for i in range(len(s)):
            if s[i] < '0' or s[i] > '9':
                s = s[:i]
                break
        if not len(s) or not s[0].isnumeric():
            return 0
        int_max = 2**31 - 1
        int_min = -(2**31)
        return max(min(int(s) * sign, int_max), int_min)

