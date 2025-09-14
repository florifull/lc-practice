class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            visited.add((r, c))
            # visit adjacent
            for roff, coff in dirs:
                if (r+roff in range(rows) and c+coff in range(cols) and 
                    (r+roff, c+coff) not in visited and grid[r+roff][c+coff] == '1'):
                    dfs(r+roff, c+coff)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    # search path
                    dfs(r, c)
                    islands += 1
        return islands
    # T: O(R * C), S: O(R * C)