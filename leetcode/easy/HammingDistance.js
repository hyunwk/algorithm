var hammingDistance = function(x, y) {
    let distance = 0;
    let xor = x^y;
    while (xor !== 0) {
        if (xor & 1) 
            distance++;
        xor = xor >> 1
    }
    return distance;
};
