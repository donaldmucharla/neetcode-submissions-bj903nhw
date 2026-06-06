class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_Set = set(nums)

        for n in num_Set:
            if n-1 in num_Set:
                continue
            length = 0
            while n in num_Set:
                length += 1
                n = n+1
            res  = max(length, res)
        
        return res