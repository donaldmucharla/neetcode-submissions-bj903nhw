class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        total = sum(nums)
        if total %2 != 0:
            return False
        target = total // 2

        for n in nums:
            nextdp = set()
            for p in dp:
                nextdp.add(p+n)
                nextdp.add(p)
            dp = nextdp
        
        return True if target in dp else False