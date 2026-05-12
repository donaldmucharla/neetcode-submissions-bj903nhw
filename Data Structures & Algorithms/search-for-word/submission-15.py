class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROW = len(board)
        COL = len(board[0])
        visited = set()

        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r, c))
            
            res = (dfs(i+1, r+1, c) or dfs(i+1, r, c+1) or dfs(i+1, r-1, c) or dfs(i+1, r, c-1))

            visited.remove((r, c))
            return res




        for r in range(ROW):
            for c in range(COL):
                if dfs(0, r, c):
                    return True
        return False
