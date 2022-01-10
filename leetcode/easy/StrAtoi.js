var myAtoi = function(s) {
    let intMax = 2**31 - 1
    let intMin = -(2**31)
    s = parseInt(s);
    if (!s)
        return 0;
    else if (s < intMin) 
        return intMin;
    else if (s > intMax) 
        return intMax;
    else
        return s;
};
