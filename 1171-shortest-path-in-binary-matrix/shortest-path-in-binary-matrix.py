class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0: return -1

        rows, cols = len(grid), len(grid[0])
        self.target = (rows-1, cols-1)
        pathL = 0
        q = collections.deque()
        grid[0][0] = 2
        q.append((0, 0))
        dirs = [[0, 1], [1, 0], [1, 1], [1, -1], [-1, 1], [0, -1], [-1, 0], [-1, -1]] # 8 dir
        while q:
            pathL += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) == self.target:
                    return pathL
                for dr, dc in dirs:
                    if (r+dr in range(rows) and c+dc in range(cols)
                        and grid[r+dr][c+dc] == 0):
                        q.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
        return -1
    # T: O(m * n), S: O(min(m, n))