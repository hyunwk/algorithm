class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, num in enumerate(nums):
            if num in target_dict:
                return [i, target_dict[num]]
            else:
                target_dict[target-num] = i

