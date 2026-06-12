class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            
            tmp = curMax * n
            curMax = max(n, tmp, curMin * n)
            curMin = min(n, tmp, curMin * n)
            res = max(curMax, res)
        return res