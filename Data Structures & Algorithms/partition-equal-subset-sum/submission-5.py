class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        if sum(nums) % 2 != 0 :
            return False
        target = sum(nums) // 2

        for n in nums:
            nextdp = set()
            for p in dp:
                nextdp.add(n+p)
                nextdp.add(p)
            dp = nextdp
        
        return True if target in dp else False
        