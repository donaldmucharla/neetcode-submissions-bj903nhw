class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                res = max(0, res)
            
            tmp = curMax * n
            curMax = max(tmp, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(curMax, res)
        return res
            