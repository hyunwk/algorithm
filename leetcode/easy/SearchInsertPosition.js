/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if (target <= nums[0])
        return 0;

    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor(left + (right-left) / 2);
        if (target == nums[mid]) 
            return mid;
        else if (target > nums[mid])
            left = mid + 1;
        else
            right = mid-1;
    }
    return left;
};
