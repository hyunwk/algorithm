/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const numerals = [{ M: 1000}, {CM: 900}, {D: 500}, {CD: 400}, {C: 100}, {XC: 90}, {L: 50}, {XL: 40}, {X: 10}, {IX: 9}, {V: 5}, {IV: 4}, {I: 1}]
    let answer = '';
    numerals.forEach((numeral) => {
        let [letter, value] = Object.entries(numeral)[0];
        if (num >= value) {
            answer += letter.repeat(Math.floor(num/value));
            num %= value
        }
    });
    return answer;
};
