class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])
        # traverse right to left, from top row down
        for r in range(rows):
            right = cols - 1
            for c in range(cols-1, -1, -1):
                # check for stationary obstacle
                if boxGrid[r][c] == '*':
                    right = c - 1
                elif boxGrid[r][c] == '#':
                    # swap right and left
                    boxGrid[r][right], boxGrid[r][c] = boxGrid[r][c], boxGrid[r][right]
                    right -= 1
        # build new matrix
        newMatrix = [['&' for r in range(rows)] for c in range(cols)]
        for r in range(rows-1, -1, -1):
            for c in range(cols):
                newMatrix[c][-r-1] = boxGrid[r][c]
        return newMatrix