class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nei = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        rows, cols = len(board), len(board[0])
        def dfs(visited, i, r, c):
            if board[r][c] != word[i]: return False
            if i == len(word)-1: return True
            visited.add((r, c))
            for dr, dc in nei:
                x, y = r+dr, c+dc
                if (x in range(rows) and y in range(cols) and 
                    (x,y) not in visited):
                    visited.add((x, y))
                    if dfs(visited, i+1, x, y): return True
                    visited.remove((x, y))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(set(), 0, r, c): return True
        return False
    # T: O(N × M × 4^L), S: O(L)