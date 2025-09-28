class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowzero, colzero = [0] * rows, [0] * cols
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowzero[r], colzero[c] = 1, 1 # 1 being "true" like a 0 has occurred here..
        # flip all non zeroes in zero occurring rows/cols (!'s) to 0's!
        for r in range(rows):
            if rowzero[r] == 1:
                # set entire row to 0's
                matrix[r] = [0] * cols
        for c in range(cols):
            if colzero[c] == 1:
                for r in range(rows):
                    # set entire column to 0's
                    matrix[r][c] = 0

    # T: O (m * n), S: O(m * n)