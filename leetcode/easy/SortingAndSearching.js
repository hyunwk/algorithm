var merge = function(nums1, m, nums2, n) {
    nums1.splice(m);
    nums1.push(...nums2);
    nums1.sort((x,y)=>x-y);
};
