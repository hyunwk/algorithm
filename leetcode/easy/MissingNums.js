/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    // if (nums.length == 1)
    //     return 1 - nums[0];
    // const sum = nums.reduce((partialSum, num) => partialSum + num, 0);
    // const len = nums.length;
    // const origin = (len+1) * len / 2; 
    // return origin - sum;

    let origin = (nums.length+1) * nums.length / 2;
    for (let num of nums) {
        origin -= num;
    }
    return origin;
};
