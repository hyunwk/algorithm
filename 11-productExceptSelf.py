from typing import List

class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            sum = 1
            for j in range(0, i):
                sum *= nums[j]
            for k in range(i+1, len(nums)):
                sum *= nums[k]
            result.append(sum)
        return result

    def productExceptSelf2(self, nums : List[int])->List[int]:
        result = []
        sum = 1
        for i in range(len(nums)):
            result.append(sum)
            sum *= nums[i]
        sum = 1
        for j in range(len(nums) -1, -1, -1):
            result[j] *= sum
            sum *= nums[j]
        return result

b = Solution()
nums = [-1,1,0,-3,3]
for i in b.productExceptSelf1(nums):
    print(i)
for i in b.productExceptSelf2(nums):
    print(i)