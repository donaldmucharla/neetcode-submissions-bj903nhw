class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        windowSum = 0
        ans = float('inf')

        for r in range(len(nums)):
            windowSum += nums[r]

            while windowSum >= target:
                ans = min(ans, (r-l+1))
                windowSum -= nums[l]
                l += 1
        
        return 0 if ans == float('inf') else ans