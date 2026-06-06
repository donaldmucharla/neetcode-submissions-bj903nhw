class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [i for i in nums]

        for i in range(len(nums)):
            res.append(nums[i])
        
        return res