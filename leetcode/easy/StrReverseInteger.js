var reverse = function(x) {
    let s = Math.abs(x).toString().split('').reverse().join('');
    if (s > 2**31)
        return 0
    return s * Math.sign(x);
};
