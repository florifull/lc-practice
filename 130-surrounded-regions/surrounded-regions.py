class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # visited serves as visited but also forbidden/edge paths..
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            # base case
            if (r not in range(rows) or c not in range(cols) or
                (r, c) in visited or board[r][c] != 'O'):
                return
            visited.add((r, c))
            board[r][c] = 'X'
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
            return
        
        def dfsForbidden(r, c):
            # base case
            if (r not in range(rows) or c not in range(cols) or
                (r, c) in visited or board[r][c] != 'O'):
                return
            visited.add((r, c))
            for dr, dc in dirs:
                dfsForbidden(r+dr, c+dc)
            return
        
        # find edge regions (or connected to edge..)
        for c in range(cols):
            # top border edge
            dfsForbidden(0, c)
            # bottom border edge
            dfsForbidden(rows-1, c)
        # edge regions for left and right boundaries
        for r in range(rows):
            # left border
            dfsForbidden(r, 0)
            # right border
            dfsForbidden(r, cols-1)
        # traverse and flip regions that ARENT connected to edge/borders
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and board[r][c] == 'O':
                    dfs(r, c)
    # T: O(m * n), S: O(m * n)