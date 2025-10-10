class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])
        # traverse boxGrid from right to left, and swap out elements accordingly
        for r in range(rows):
            e_pt = [r, cols-1]
            for c in range(cols-1, -1, -1): # don't need to check leftmost (0th col.)
                coordVal = boxGrid[r][c]
                if coordVal == '.':
                    continue
                elif coordVal == '*':
                    e_pt = [r, c-1]
                else: # stone found
                    e_r, e_c = e_pt[0], e_pt[1]
                    boxGrid[e_r][e_c], boxGrid[r][c] = coordVal, boxGrid[e_r][e_c]
                    e_pt = [e_r, e_c-1]
        # traverse from (bottom) left to right -> row, col -> col, row
        newBox = [['' for r in range(rows)] for c in range(cols)]
        # now I need to traverse new matrix and fill in corresponding rotated points
        for r in range(rows-1, -1, -1):
            for c in range(cols):
                newBox[c][rows - 1 - r] = boxGrid[r][c]
        return newBox
    # T: O(n * m), S: O(n * m)