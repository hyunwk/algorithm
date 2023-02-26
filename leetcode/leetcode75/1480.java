class Solution {
    public int[] runningSum(int[] nums) {
        for (int idx=1 ;idx < nums.length ; idx += 1 ) {
            nums[idx] += nums[idx-1];
        }
        return nums;
    }
}
