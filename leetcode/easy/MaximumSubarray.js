var maxSubArray = function(nums) {
    let dp = Array(nums.length);
    dp[0] = nums[0];
    for (let idx=1; idx<nums.length ; idx++) {
        dp[idx] = nums[idx] + (dp[idx-1] >= 0 ? dp[idx-1] : 0)
    }
    return Math.max(...dp);
};
