var threeSumClosest = function(nums, target) {
    if (nums.length < 3)
        return [];
    nums.sort((a,b)=>a-b);
    let closest = 10000
    
    for (let i=0 ; i<nums.length-2 ; i++) {
        let low = i+1;
        let high = nums.length-1;
        while (low < high) {
            const sum = nums[i] + nums[low] + nums[high];
            if (sum == target)
                return sum;
            else if (sum < target)
                low++;   
            else if (sum > target) 
                high--;  
            
            if (Math.abs(closest - target) > Math.abs(sum - target))
                closest = sum;
        }    
    }
    return closest;
};
