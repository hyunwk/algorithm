var rotate = function(matrix) {
    matrix.reverse()
    let temp;
    for (let i=0; i<matrix.length ; i++) {
        for (let j=0; j<i ; j++) {
            temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    return matrix;
};
