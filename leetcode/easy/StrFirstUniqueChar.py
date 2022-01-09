class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = [chr(c) for c in range(ord('a'), ord('z')+1)]
        lst = [s.index(c) for c in alphabets if s.count(c) == 1]
        return min(lst) if len(lst) else -1
