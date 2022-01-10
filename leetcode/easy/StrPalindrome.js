var isPalindrome = function(s) {
    let l = 0;
    let r = s.length - 1;
    s = s.replace(/[^0-9a-z]/gi,'').toLowerCase();
    return s == s.split('').reverse().join('');
};
