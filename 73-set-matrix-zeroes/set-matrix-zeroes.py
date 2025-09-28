class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        def makeZero(r, c):
            # change entire column
            for row in range(rows):
                if matrix[row][c] != 0: matrix[row][c] = '!'
            # change entire row
            for col in range(cols):
                if matrix[r][col] != 0: matrix[r][col] = '!'
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    makeZero(r, c)
        # flip all non zeroes in zero occurring rows/cols (!'s) to 0's!
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '!': matrix[r][c] = 0
    # T: O (m * n), S: O(1)