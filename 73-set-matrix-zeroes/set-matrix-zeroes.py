class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        # denote ea non zero in a 0 row/col with a '*'
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # mark all rows to be flipped (*)
                    for row in range(rows):
                        if matrix[row][c] != 0 and matrix[row][c] != '*':
                            matrix[row][c] = '*'
                    # mark all cols to be flipped (*)
                    for col in range(cols):
                        if matrix[r][col] != 0 and matrix[r][col] != '*':
                            matrix[r][col] = '*'
        # we've marked all coords that need to be flipped to 0's - now find em!
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '*':
                    matrix[r][c] = 0
    # T: O(m * n + (n + m)), S: O(1)