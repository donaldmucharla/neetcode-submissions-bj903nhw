class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL =len(matrix), len(matrix[0])
        top, bot = 0, ROW-1

        while top <= bot:
            mid_row =(top+bot) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row -1
            else:
                break
        
        if not (top <= bot):
            return False

        l, r = 0, COL-1
        
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid_row][mid] > target:
                r = mid-1
            elif matrix[mid_row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False