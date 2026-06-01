class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) //2

        for n in nums:
            next_dp = set()
            for d in dp:
                next_dp.add((d + n))
                next_dp.add((d))
            dp = next_dp
            if target in dp:
                return True
        
        return target in dp
