class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(r, c, prev, visited):
            # base case
            if (r not in range(rows) or c not in range(cols) or
                (r, c) in visited or heights[r][c] < prev):
                return
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc, heights[r][c], visited)
            return
        # loop over top and bottom borders (pacfic & atlantic)
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows-1, c, heights[rows-1][c], atl)
        # loop over left and right borders (pacific & atlantic)
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols-1, heights[r][cols-1], atl)
        # return intersection of both lists
        return list(pac & atl)
    # T: O(m * n), S: O(m * n)