/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    const getPalindrome = (left, right) => {
        while (0<=left && right<s.length && s[left] == s[right]) {
            left--;
            right++;
        }
        return s.slice(left+1, right);
    };
    
    if (s.length == 1) return s;
    let palindromes = [];
    for (let i=0; i<s.length-1 ; i++) {
        palindromes.push(getPalindrome(i, i+1));
        palindromes.push(getPalindrome(i-1, i+1));    
    }
    return palindromes.reduce((a,b) => a.length > b.length ? a : b);
};
