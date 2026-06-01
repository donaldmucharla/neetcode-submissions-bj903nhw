class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, curSum):
            if i >= len(nums):
                return 1 if curSum == target else 0
            
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            
            add = dfs(i+1, curSum+ nums[i])
            sub = dfs(i+1, curSum - nums[i])

            dp[(i, curSum)] = add + sub 
            return dp[(i, curSum)]
        
        return dfs(0, 0)
