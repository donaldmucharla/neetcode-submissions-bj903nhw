class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for n in nums:
            next_dp = set()
            for t in dp:
                if t + n == target:
                    return True

                next_dp.add(t+n)
                next_dp.add(t)
            dp = next_dp

        return False
        