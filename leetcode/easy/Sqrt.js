var mySqrt = function(x) {
//     if (!x) return 0;
    
//     let sqrt = 1;
//     while (sqrt*sqrt <= x)
//         sqrt++;
//     return sqrt-1;
    if (x <= 1) return x;
    
    let left = 0;
    let right = x;
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (mid*mid == x){
            return mid;
        }
        else if (mid*mid > x) {
            right = mid;
        }
        else {
            left = mid + 1;
        }
    }
    return left - 1;
};
