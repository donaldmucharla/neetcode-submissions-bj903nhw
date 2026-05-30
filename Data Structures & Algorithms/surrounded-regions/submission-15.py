class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL =len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or board[r][c] != "O":
                return
            
            board[r][c] = "T"

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(ROW):
            for c in range(COL):
                if (r  == 0 or r == ROW-1 or c == 0 or c == COL-1) and board[r][c] == "O":
                    dfs(r, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        





