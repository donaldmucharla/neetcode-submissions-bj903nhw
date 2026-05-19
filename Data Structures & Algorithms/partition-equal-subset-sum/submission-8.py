class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        total  = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        for n in nums:
            nextDp = set()
            for d in dp:
                nextDp.add(n+d)
                nextDp.add(d)
            dp = nextDp
        
        return True if target in dp else False
        