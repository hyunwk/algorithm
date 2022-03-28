var fourSum = function(nums, target) {
    const result = [];
    const current = [];
    if (nums.length < 4)
        return result;
    nums.sort((a,b)=>a-b);
    
    const kSum = (k, start, target) => {
        if (k!=2) {
            for (let i=start ; i<nums.length-k+1 ; i++)
            {
                if (i>start && nums[i] == nums[i-1])
                    continue
                current.push(nums[i])
                kSum(k-1, i+1, target - nums[i]);
                current.pop(); 
            }
            return ;
        }
        let [l, r] = [start, nums.length-1];
        while (l < r) {
            let sum = nums[l] + nums[r]
            if (sum > target) {
                r--;
            } else if (sum < target) {
                l++;
            } else {
                result.push([...current, nums[l], nums[r]]);
                l++;
                while (nums[l] == nums[l-1])
                    l++;
            }
        }
    };
    kSum(4, 0, target);
    return result;
};
