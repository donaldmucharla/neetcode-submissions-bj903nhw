class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        top = 0
        bot = ROW-1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break
        
        if not (top <= bot):
            return False

        l = 0
        r = COL-1

        row = (top + bot) // 2

        # Step 2: Binary search in that row
        l, r = 0, COL - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True

        return False

        
        