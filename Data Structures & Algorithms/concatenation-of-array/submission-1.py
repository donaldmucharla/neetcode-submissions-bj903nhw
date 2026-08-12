class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [i for i in nums]

        for i in nums:
            ans.append(i)
    
        return ans