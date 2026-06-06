class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        curSum = 0
        count = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            if diff in seen:
                count += seen[diff]
            
            seen[curSum] = 1 + seen.get(curSum, 0)
        
        return count