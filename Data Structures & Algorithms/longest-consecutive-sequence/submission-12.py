class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in nums:
            if n-1 not in num_set:
                length = 1
                while n+1 in num_set:
                    length += 1
                    n += 1
                
                longest = max(longest, length)
            
        return longest

