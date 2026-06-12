class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        visited = set()
        visited.add(0)

        for n in nums:
            next_set = set()
            for v in visited:
                next_set.add(v+n)
                next_set.add(v)
            if target in next_set:
                return True
            visited = next_set
        
        return False
            

