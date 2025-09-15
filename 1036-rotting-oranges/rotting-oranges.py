class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = rotten = totalOranges = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        # traverse grid for all oranges (fresh AND rotten)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    fresh += 1
                    totalOranges += 1
                elif grid[r][c] == 2:
                    rotten += 1
                    q.append((r, c))
                    totalOranges += 1
        # edge cases
        if rotten == 0 and fresh: return -1
        if totalOranges == 0 or fresh == 0: return 0
        # bfs
        while q and rotten != totalOranges:
            for _ in range(len(q)):
                r, c = q.popleft()
                for roff, coff in dirs:
                    newR, newC = r+roff, c+coff
                    if (newR in range(rows) and newC in range(cols)
                    and grid[newR][newC] == 1):
                        # fresh orange becomes rotten (val 2)
                        grid[newR][newC] = 2
                        rotten += 1
                        q.append((newR, newC))
            minutes += 1
        return -1 if rotten != totalOranges else minutes
    # T: O(r * c), S: O(r * c)