class Solution {
    public int pivotIndex(int[] nums) {
        int left_sum = 0;
        int whole_sum = Arrays.stream(nums).sum();
        
        for (int i=0 ; i< nums.length ; i++) {
            if (left_sum * 2 + nums[i]== whole_sum) {
                return i;
            }
            left_sum += nums[i];
        }
        return -1;
    }
}
