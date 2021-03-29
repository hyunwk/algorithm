from typing import List

class Solution:
    def trap1(self, height:List[int])->int :
        left, right = 0, len(height) - 1
        volume = 0
        left_max = height[left]
        right_max = height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left])\
                                , max(right_max, height[right])
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else :
                volume += right_max - height[right]
                right -= 1
        return volume

    def trap2(self, height : List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume


b = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(b.trap1(height))
print(b.trap2(height))
