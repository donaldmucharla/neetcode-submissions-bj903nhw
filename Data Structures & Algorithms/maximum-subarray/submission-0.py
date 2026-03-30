class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum =nums[0]
        
        for i in range(len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            maxsum = max(cursum, maxsum)
        

        return maxsum