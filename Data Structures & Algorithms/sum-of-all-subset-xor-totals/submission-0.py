class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def dfs(i, curSum):
            nonlocal total
            if i == len(nums):
                total += curSum
                return
            
            dfs(i+1, curSum ^ nums[i])
            dfs(i+1, curSum)

        
        dfs(0, 0)
        return total

            