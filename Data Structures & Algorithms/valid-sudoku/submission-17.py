class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = collections.defaultdict(set)
        COL = collections.defaultdict(set)
        Square = collections.defaultdict(set)
        row = len(board)
        col = len(board[0])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if r < 0 or c < 0 or r > row or c > col or board[r][c] in ROW[r] or board[r][c] in COL[c] or board[r][c] in Square[(r//3, c//3)]:
                    return False
                ROW[r].add(board[r][c])
                COL[c].add((board[r][c]))
                Square[(r//3, c//3)].add(board[r][c])
        return True