// JavaScript
// Use >>>* instead of >>. This is as same as Java.

// After |, &, ~, >>, <<, the number was converted ToInt32. But you need return a positive value. So try return result >>> 0;. >>> will call ToUint32*.
var reverseBits = function(n) {
    let result = 0;
    for (let i = 0; i<32 ; i++) {
        result <<= 1;
        result += n & 1;       
        n >>= 1;
    }
    console.log('>>', (result >> 0).toString(2));
    console.log('>>>', (result >>> 0).toString(2));
    return result >>> 0;
};
