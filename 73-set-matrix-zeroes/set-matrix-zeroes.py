class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        firstRowZero = any(matrix[0][c] == 0 for c in range(cols))
        firstColZero = any(matrix[r][0] == 0 for r in range(rows))

        # traverse inner matrix and check for 0's
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c], matrix[r][0] = 0, 0
        
        # traverse inner matrix and change appropriate cells to 0's
        for r in range(1, rows):
            for c in range(1, cols):
                # check top row and top col for 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # traverse through borders and make 0's appropriately
        if firstRowZero:
            for c in range(cols):
                matrix[0][c] = 0
        if firstColZero:
            for r in range(rows):
                matrix[r][0] = 0