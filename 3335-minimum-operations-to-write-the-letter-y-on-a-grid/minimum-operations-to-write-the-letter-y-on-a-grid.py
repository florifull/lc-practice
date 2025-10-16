class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # repy = integers for "Y" shape, repo = integers for everything else..
        def traversal(repy, repo):
            rows, cols = len(grid), len(grid[0])
            midcol, midrow = cols // 2, rows // 2
            rep = 0
            for i in range(rows):
                for j in range(cols):
                    # check for coord part of 'Y'...
                    #   left top 'Y'
                    if ((i == j and j <= midcol) or
                        # right top 'Y'
                        (i + j == cols-1 and j > midcol) or
                        # bottom half of 'Y'
                        (i > midrow and j == midrow)):
                        if grid[i][j] != repy: rep += 1
                    # not part of y..
                    elif grid[i][j] != repo: rep += 1
            return rep

        minOperations = float('inf')
        combos = [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]
        for repy, repo in combos:
            minOperations = min(minOperations, traversal(repy, repo))
        return minOperations
    # T: O(m * n), S: O(1)