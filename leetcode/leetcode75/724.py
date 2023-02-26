class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # whole_sum = sum(nums)
        # for i in range(len(nums)):
        #     left_sum = sum(num for num in nums[:i])
        #     if left_sum * 2 + nums[i] == whole_sum:
        #     # same as (if left_sum == right_sum)
        #         return i
        # return -1

        left_sum = 0
        right_sum = sum(nums)

        for idx, num in enumerate(nums):
            left_sum += num
            if left_sum == right_sum:
                return idx
            right_sum -= num
        return -1
