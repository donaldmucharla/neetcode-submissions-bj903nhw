class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for n in nums:
            if n-1 in num_set:
                continue
            longest = 0
            while n in num_set:
                longest += 1
                n += 1
            
            res = max(res, longest)
        return res