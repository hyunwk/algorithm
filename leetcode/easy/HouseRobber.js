var rob = function(nums) {
    if (nums.length <= 2) {
        return Math.max(...nums);
    }
    let dp = Array(nums.length);
    dp[0] = nums[0];
    dp[1] = Math.max(dp[0], nums[1]);
    for (let idx=2; idx<nums.length ; idx++) {
        dp[idx] = Math.max(dp[idx-2] + nums[idx], dp[idx-1]);
    }
    console.log(dp)
    return Math.max(...dp);
};
