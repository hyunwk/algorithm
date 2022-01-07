var intersect = function(nums1, nums2) {
    counter = {};
    result = [];
    nums1.forEach((num1) => {
        if (num1 in counter) {
            counter[num1]++;
        } else {
            counter[num1] = 1;
        }
    })
    nums2.forEach((num2) => {
        if (num2 in counter && counter[num2]) {
            result.push(num2);
            counter[num2]--;
        }
    })
    return result;
};
