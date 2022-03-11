var lengthOfLongestSubstring = function(s) {
    let row = [];
    let maxLength = 0;
    
    if ([...new Set(s)].length === 1)
        return 1
    for (let index=0; index<s.length ; index++) {
        if (row.includes(s[index])) {
            row = row.slice(row.indexOf(s[index])+1, row.length);
            row.push(s[index]);
        } else {
            row.push(s[index]);
            if (row.length > maxLength) 
                maxLength = row.length;
        }
    }
    return maxLength;
};

var lengthOfLongestSubstring = function(s) {
    let map = new Map();
    let maxLength = 0;
    for (let c=1 ; c<=127 ; c++) {
        map.set(c,-1);
    }
    let start = -1;
    for (let index=0 ; index<s.length ; index++) {
        if (map.get(s[index]) > start)
            start = map.get(s[index])
        map.set(s[index],index);
        maxLength = Math.max(maxLength, index - start)
    }
    return maxLength;
}
