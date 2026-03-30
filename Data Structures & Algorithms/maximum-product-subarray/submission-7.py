class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1. Initialize result with the first element
        res = nums[0]
        curMin, curMax = 1, 1
        
        for n in nums:
            # 2. Handle zero: reset products to 1 
            # (Though the math below handles 0, this keeps it clean)
            if n == 0:
                curMin, curMax = 1, 1
                res = max(res, 0)
                continue
            
            # 3. Important: Store curMax before updating it
            tmp = curMax * n
            
            # 4. Update max and min simultaneously
            # We compare: the number itself, n * old_max, and n * old_min
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            # 5. Update the global maximum
            res = max(res, curMax)
            
        return res