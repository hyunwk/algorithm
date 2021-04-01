from typing import List

class Solution:
    def arrayPairSum1(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum

    def arrayPairSum2(self, nums: List[int])->int:
        sum = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum

    def arrayPairSum3(self, nums: List[int])->int:
        return sum(sorted(nums)[::2])

nums = [6,2,6,5,1,2]
b = Solution()
print(b.arrayPairSum1(nums))
print(b.arrayPairSum2(nums))
print(b.arrayPairSum3(nums))
