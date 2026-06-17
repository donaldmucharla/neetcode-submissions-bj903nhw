class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        dp = [False] * (len(nums))

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if dp[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not dp[i-1]:
                    continue
                path.append(nums[i])
                dp[i] = True
                dfs(path)
                path.pop()
                dp[i] = False
        
        dfs([])
        return res

                


