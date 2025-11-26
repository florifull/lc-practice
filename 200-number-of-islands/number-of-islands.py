class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        adj = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in adj:
                if (r+dr in range(rows) and c+dc in range(cols)
                    and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == '1'):
                    dfs(r+dr, c+dc)
            return

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands
    # T: O(m * n), S: O(m * n) - optimize via changing cell to * or etc out of bound input