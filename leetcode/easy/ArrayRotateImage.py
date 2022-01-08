class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # using zip
        matrix[:] = map(list, zip(*matrix[::-1]))
        # using for
        matrix[:] = matrix[::-1]
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
