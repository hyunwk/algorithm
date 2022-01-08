class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
# using 
        def check_valid(nums):
            return sum(nums) == sum(set(nums))
        # row
        for row in range(9):
            nums = []
            for col in range(9):
                num = board[row][col]
                if  num != '.':
                    nums.append(int(num))
            if not check_valid(nums):
                return False 

        # column
        for row in range(9):
            nums = []
            for col in range(9):
                num = board[col][row]
                if  num != '.':
                    nums.append(int(num))
            if not check_valid(nums):
                return False 
        # box
        def check_box(i, j):
            nums = []
            for row in range(3):
                for col in range(3):
                    num = board[i + row][j + col]
                    if  num != '.':
                        nums.append(int(num))
            return check_valid(nums)

        for i in range(0,9,3):
            for j in range(0,9,3):
                if not check_box(i, j):
                    return False
        return True

# using set len
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += ((i,c), (c, j), (i//3, j//3, c))
        return len(seen) == len(set(seen))
