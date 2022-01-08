//two pointer
var moveZeroes = function(nums) {
    let slow = 0;
    for (let fast=0; fast < nums.length ; fast+=1) {
        if (nums[fast] && nums[slow] == 0) {
            nums[slow] = nums[fast];
            nums[fast] = 0;
        }
        if (nums[slow]) {
            slow += 1;
        }
    }
    return nums
};
