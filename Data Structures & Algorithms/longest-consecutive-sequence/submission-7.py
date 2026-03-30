class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for n in nums:
            if n-1 not in nums:
                current = n
                lenght = 1

                while current + 1 in nums:
                    current += 1
                    lenght += 1
                longest = max(longest, lenght)
        
        return longest