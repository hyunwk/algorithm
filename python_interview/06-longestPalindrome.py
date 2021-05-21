from builtins import str


class Solutions:
    def logestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int)->str:
            while 0 <= left and right < len(str) - 1 and str[left] == str[right]:
                left -= 1
                right += 1
            return str[left + 1 : right]

        if len(str) < 2 or s[:] == s[::-1]:
            return s

        result = ' '
        for i in range(0, len(s) - 1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key = len)
        return result

str = "aa"
f = Solutions()
print(f.logestPalindrome(str))