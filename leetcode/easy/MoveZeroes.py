class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
# pop and append
        nums = [0,1,0,3,12]
        zero_cnt = 0
        i = 0
        while i < len(nums): 
            if not nums[i]:
                nums.pop(i)
                zero_cnt+=1
            else:
                i+=1
        
        for _ in range(zero_cnt):
            nums.append(0)
        
        return nums

# two pointer
        slow = 0;
        for fast in range(len(nums)):
            if nums[fast] and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow]:
                slow += 1
