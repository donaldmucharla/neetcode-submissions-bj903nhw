class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0

        while r < len(nums)-1:
            fartest = 0
            for i in range(l, r+1):
                fartest = max(fartest, nums[i]+i)
            
            l = r + 1
            r = fartest
            res += 1
        return res



        