var plusOne = function(digits) {
    // num = +digits.join('') + 1;
    // return Array.from(num.toString());
	// js의 number 자료형 크기 때문에 불가
    let i=digits.length - 1;
    for (i ; i>=0 ; i--) {
        digits[i]++;
        if (digits[i] > 9) {
            digits[i] = 0;
        } else {
            return digits;
        }
    }
    return [1, ...digits]
};
