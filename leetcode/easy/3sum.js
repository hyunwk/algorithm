/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const check_target = (i) => {
        let low = i+1;
        let high = nums.length-1;
        while (low < high) {
            const sum = nums[i] + nums[low] + nums[high];

            if (sum == target) {
                result.push([nums[i], nums[low], nums[high]]);
                while (nums[low] == nums[low+1])
                    low++;
                while (nums[high] == nums[high-1])
                    high--;
                low++;
                high--;
            } 
            else if (sum < target)
                low++;
            else
                high--;
        }    
    }
    
    if (nums.length < 3)
        return [];
    nums.sort((a,b)=>a-b);
    
    const result = [];
    const target = 0;
    
    for (let i=0 ; i<nums.length-2 ; i++) {
        if (nums[i] > target) 
            break;
        
        if (i>0 && nums[i] == nums[i-1]) 
            continue;
        
        check_target(i);
    }
    return result;
};
