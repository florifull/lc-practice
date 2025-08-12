class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        squares = collections.defaultdict(set)
        visitedCol = collections.defaultdict(set)
        for r in range(rows):
            visitedRow = set()
            for c in range(cols):
                if board[r][c] == '.': continue
                if (board[r][c] in visitedRow or
                    board[r][c] in visitedCol[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                visitedRow.add(board[r][c])
                visitedCol[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
