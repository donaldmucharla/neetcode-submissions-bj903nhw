class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."]*n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(board[i]) for i in range(n)]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = "."
        dfs(0)
        return res
        