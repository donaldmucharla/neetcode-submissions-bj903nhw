class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW = [1] * n

        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + ROW[j]
            
            ROW = new_row
        
        return ROW[0]