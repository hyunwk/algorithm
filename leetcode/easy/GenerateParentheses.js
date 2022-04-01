/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const answer = [];
    
    const addPair = (pairString, open, close) => {
        if (open == 0 && close == 0) {
            answer.push(pairString);
            return ;
        }
        
        if (open) addPair(pairString+'(', open-1, close);
        if (open < close) addPair(pairString+')', open, close-1);
    }
    addPair('', n, n);
    return answer;
};
