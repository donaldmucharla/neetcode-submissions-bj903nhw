class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
      
        if not matrix or not matrix[0]:
            return 0 
        ROW = len(matrix)
        COL = len(matrix[0])
        longest = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dp = [[0] * COL for _ in range(ROW)]

        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            matrix_path = 1
            for dr, dc in directions:
                nr = r + dr
                nc= c + dc

                if nr >=0 and nr < ROW and nc >=0 and nc < COL and matrix[nr][nc] > matrix[r][c]:
                    matrix_path = max(matrix_path, 1 + dfs(nr, nc))
            
            dp[r][c] = matrix_path
            return matrix_path

        


        for r in range(ROW):
            for c in range(COL):
                longest =  max(longest, dfs(r, c))
        
        return longest