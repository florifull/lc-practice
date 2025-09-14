class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, localArea):
            visited.add((r, c))
            localArea = 1
            for roff, coff in dirs:
                # check adjacents
                if (r+roff in range(rows) and c+coff in range(cols)
                    and grid[r+roff][c+coff] == 1 and (r+roff, c+coff) not in visited):
                    localArea += dfs(r+roff, c+coff, localArea)
            return localArea
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    localA = dfs(r, c, 0)
                    if localA > maxArea: maxArea = localA
        return maxArea