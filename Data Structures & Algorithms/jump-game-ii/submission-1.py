class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l, r = 0,0

        while r < (len(nums)-1):
            farther = 0
            for i in range(l, r+1):
                farther = max(farther, i+nums[i])
            l = r+1
            r = farther
            res+= 1
        
        return res

        