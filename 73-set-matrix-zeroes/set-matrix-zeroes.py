class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        topLeftRowZero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0: matrix[0][0] = 0
                    if c == 0: topLeftRowZero = True
                    else:
                        # set top boundary
                        matrix[0][c] = 0
                        # set left boundary
                        matrix[r][0]  = 0
        # traverse through inner matrix (not touching borders)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] != 0:
                    # check top border and left border
                    if matrix[0][c] == 0 or matrix[r][0] == 0: matrix[r][c] = 0
        # only traverse through borders if top left is 0..
        if matrix[0][0] == 0:
            # traverse through top border
            for c in range(cols):
                if matrix[0][c] != 0: matrix[0][c] = 0
        if topLeftRowZero:
            # traverse through leftmost border
            for r in range(rows):
                if matrix[r][0] != 0: matrix[r][0] = 0