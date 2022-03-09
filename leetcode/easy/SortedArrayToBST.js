var sortedArrayToBST = function(nums) {
    if (nums.length === 0) 
        return null;
    const makeBst = (low, high) => {
        if (low > high) 
            return null;
        
        let mid = parseInt((low + high) / 2);
        return new TreeNode(
            nums[mid],
            makeBst(low, mid-1),
            makeBst(mid+1, high)  
        );
    }
    return makeBst(0, nums.length-1);
};
