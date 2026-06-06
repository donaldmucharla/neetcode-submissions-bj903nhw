class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        n = len(nums)
        left_Sum = [1] * n

        for l in range(n):
            left_Sum[l] = left
            left = left * nums[l]

        right = 1
        right_sum = [1] * n
        for r in range(n-1, -1, -1):
            right_sum[r] = right
            right = right * nums[r]
        
        res = [1] * n
        for i in range(n):
            res[i] = left_Sum[i] * right_sum[i]
        
        return res
            