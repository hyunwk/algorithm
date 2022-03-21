/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    // let result = [[1]];
    // for (let i=1 ; i<numRows ; i++) {
    //     result.push([])
    //     result[i][0] = result[i][i] = 1;
    //     for (let j=1 ; j<i ; j++)
    //         result[i][j] = result[i-1][j-1] + result[i-1][j];
    // }
    // return result;
    let result = [[1]];
    for (let i=1 ; i<numRows ; i++) {
        left = [...result[i-1], 0];
        right = [0, ...result[i-1]];
        let newRow = left.map((item, index) => item + right[index]);
        result.push(newRow);
    }
    return result;
};
