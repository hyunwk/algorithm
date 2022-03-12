var climbStairs = function(n) {
    let dp = Array(n+1)
    dp[1] = 1; // one way to climb up step 1
    dp[2] = 2;// two way to climb up step 2
              // climb up step 3 is equal to climb from step 1, 2
    
    for (let index=3; index<=n ; index++) {
        dp[index] = dp[index-1] + dp[index-2];
    }
    return dp[n];
};
