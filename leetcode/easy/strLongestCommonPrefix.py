class Solution:
    def longestCommonPrefix(self,strs) -> str:
        # binary search
        left, right = 0, len(min(strs, key=len))
        answer = ""
        while left <= right:
            mid = (left + right) // 2
            idx = 0
            while idx < len(strs) - 1:
                if strs[idx][:mid] == strs[idx+1][:mid]:
                    idx += 1
                else:
                    right = mid - 1
                    break
            if idx == len(strs) - 1:
                answer = strs[0][:mid]
                left = mid + 1

        return answer
        
    def longestCommonPrefix2(self,strs) -> str:
        for idx, s in enumerate(zip(*strs)):
            if len(set(s)) > 1:
                return strs[0][:idx]
        return min(strs)
