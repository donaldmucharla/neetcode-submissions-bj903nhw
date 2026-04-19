class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL  =  len(board), len(board[0])

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
                if  board[r][c] == "O" and (r in [0, ROW-1] or c in [0, COL-1]):
                    dfs(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "T":
                    board[r][c] = "O"
    
