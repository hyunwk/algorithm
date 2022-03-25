/**
 * @param {number[]} height
 * @return {number}
 */

// Idea / Proof:

// 1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
// 2. All other containers are less wide and thus would need a higher water level in order to hold more water.
// 3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

var maxArea = function(height) {
    let i = 0;
    let j = height.length - 1;
    let maxAmount = 0;
    while (i<j) {
        maxAmount = Math.max(maxAmount, (j-i)*Math.min(height[i], height[j]));
        if (height[i] < height[j])
            i++;
        else
            j--;
    }
    return maxAmount;
};
