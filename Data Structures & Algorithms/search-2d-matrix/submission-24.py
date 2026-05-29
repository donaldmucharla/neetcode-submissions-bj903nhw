class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        top = 0
        bot = ROW-1

        while top <= bot:
            mid = (bot+top)//2
            if target < matrix[mid][0]:
                bot = mid-1
            elif target > matrix[mid][-1]:
                top = mid+1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l = 0 
        r = COL-1
        row =  (top + bot) // 2

        while l <= r:
            mid = (l+r)//2

            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                r = mid-1
            else:
                l = mid+1
        
        return False
            