class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols)
                or grid[r][c] != 1 or (r, c) in visited):
                return 0
            visited.add((r, c))
            localA = 1
            for roff, coff in dirs:
                # check adjacents
                localA += dfs(r+roff, c+coff)
            return localA

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    localA = dfs(r, c)
                    if localA > maxArea: maxArea = localA
        return maxArea
    #T: 