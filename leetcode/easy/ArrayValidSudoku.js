var isValidSudoku = function(board) {
    let seen = new Set();
    for (let i=0; i < board.length ; i++) {
        for (let j=0; j < board[i].length ; j++) {
            c = board[i][j]
            if (c != '.') {
                rowCell = `row ${i} ${c}`;
                colCell = `col ${c} ${j}`;
                boxCell = `box ${parseInt(i/3)} ${parseInt(j/3)} ${c}`;
                if (seen.has(rowCell) || seen.has(colCell) || seen.has(boxCell)) {
                    return false;
                }
                seen.add(rowCell);
                seen.add(colCell);
                seen.add(boxCell);
          }
        }
    }
    return true;
};
