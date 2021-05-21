from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, curr in enumerate(T):
            while stack and curr > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

T = [73, 74, 75, 71, 69, 72, 76, 73]
b = Solution()
for i in b.dailyTemperatures(T):
    print(i)
