/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if (target <= nums[0])
        return 0;

    let left = 0;
    let right = nums.length;

    while (left < right) {
        let mid = Math.floor(left + (right-left) / 2);
        if (target == nums[mid]) 
            return mid;
        else if (target < nums[mid])
            right = mid;
        else
            left = mid+1;
    }
    return left;
};
