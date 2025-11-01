class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols)
                or (r, c) in visited or grid[r][c] != '1'):
                return
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands