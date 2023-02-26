class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for idx, num in enumerate(nums):
        #     if idx == 0:
        #         continue
        #     nums[idx] = nums[idx-1] + num

        # return nums

        for idx in range(1, len(nums)):
            nums[idx] = nums[idx-1] + nums[idx]
        return nums
