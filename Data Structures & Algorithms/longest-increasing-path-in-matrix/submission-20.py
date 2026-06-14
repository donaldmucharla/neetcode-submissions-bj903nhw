class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        ROW = len(matrix)
        COL = len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            length = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or matrix[nr][nc] <= matrix[r][c]:
                    continue
                length = max(length, 1+dfs(nr, nc))
            dp[(r, c)] = length
            
            return dp[(r, c)]
        ans = 0
        for r in range(ROW):
            for c in range(COL):
                ans = max(ans, dfs(r, c))
        
        return ans

