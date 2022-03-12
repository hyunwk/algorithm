var solution = function(isBadVersion) {
    return function(n) {
        let low = 1;
        let high = n;
        while (low < high) {  
            let mid = Math.floor(low + (high-low) / 2);
            if (isBadVersion(mid)) {
                high = mid;
            } else {
                low = mid+1;
            }
        }
        return low;
    };
};
