class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            first, temp, cnt = s[0], '', 0
            for l in s:
                if first == l:
                    cnt += 1
                else:
                    temp += str(cnt) + first
                    first = l
                    cnt = 1
            temp += str(cnt) + first
            s = temp
        return s
