/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if (s.length % 2 == 1)
        return false;
    
    let parentheses = {
        '{' : '}',
        '[' : ']',
        '(' : ')',
    };
    let stack = [];
    
    for (let i=0; i<s.length ; i++) {
        let c = s.charAt(i);
        if (Object.keys(parentheses).includes(c)) {
            stack.push(c);
        } 
        else {
            let before = stack.pop();
            if (parentheses[before] !== c)
                return false;
        }
    }
    return stack.length === 0;
};
