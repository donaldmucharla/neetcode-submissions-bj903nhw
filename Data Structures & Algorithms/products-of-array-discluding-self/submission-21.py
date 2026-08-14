class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        left_sum = [1] * len(nums)
        for l in range(len(nums)):
            left_sum[l] = left
            left = left * nums[l]
        

        right = 1
        right_sum = [1] * len(nums)
        for r in range(len(nums)-1, -1, -1):
            right_sum[r] = right
            right = right * nums[r]
        
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = left_sum[i] * right_sum[i]
        
        return res
