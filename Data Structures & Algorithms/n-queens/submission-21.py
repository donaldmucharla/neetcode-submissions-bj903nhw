class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDia = set()
        posDia = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            
            for c in range(n):
                if c in col or (r-c) in negDia or (r+c) in posDia:
                    continue
                
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)

                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return res



        