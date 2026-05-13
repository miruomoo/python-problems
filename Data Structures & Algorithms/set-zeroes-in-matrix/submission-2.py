class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    for i in range(rows):
                        if matrix[i][col] != 0:
                            matrix[i][col] = -1
                    for i in range(cols):
                        if matrix[row][i] != 0:
                            matrix[row][i] = -1

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == -1:
                    matrix[row][col] = 0
                    