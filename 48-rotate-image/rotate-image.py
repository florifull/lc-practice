class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose, and then reflect (on y axis)
        # ex: 3 @ [0, 2] -> [2, 0]
        rows = cols = len(matrix) # "nxn matrix.."
        # transpose (swapping x,y with y,x)
        for r in range(rows):
            for c in range(r, rows):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # reflect
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(rows):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l, r = l + 1, r - 1