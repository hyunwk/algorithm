/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let quotient = 0;
    let isNegative = false;
    if ((dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0))
        isNegative = true;
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    
    while (dividend >= divisor) {
        let tempDivisor = divisor;

        while (tempDivisor <= (dividend>>1)) {
            tempDivisor <<= 1;
        }
        dividend -= tempDivisor;
        quotient += tempDivisor / divisor;
    }
    
    if (quotient > 2**31 && isNegative)
        return -(2**31);
    if (quotient > 2**31-1 && !isNegative)
        return 2**31-1
    return isNegative ? -quotient : quotient; 
};
