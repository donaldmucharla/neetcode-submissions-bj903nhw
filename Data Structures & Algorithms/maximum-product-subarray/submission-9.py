class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                res = max(res, 0)
                continue
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(curMax, res)
        return res
        