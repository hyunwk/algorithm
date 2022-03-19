/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    // s = s.replace("IV", "IIII").replace("IX", "VIIII")
    // s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    // s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    // let converters = {
    //     'I':1,
    //     'V':5,
    //     'X':10,
    //     'L':50,
    //     'C':100,
    //     'D':500, 
    //     'M':1000
    // }
    // let sum=0;
    // for (let c of s) {
    //     sum += converters[c]
    // }
    // return sum;

    let converter = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500, 
        'M':1000
    }
    let sum=0;
    for (let i=0 ; i<s.length-1 ; i++) {
        converter[s[i]] >= converter[s[i+1]]
        ? sum += converter[s[i]]
        : sum -= converter[s[i]]
    }
    return sum + converter[s.at(-1)];
    
};
