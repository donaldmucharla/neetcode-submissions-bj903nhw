class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if val != nums[r]:
                nums[l] = nums[r]
                l += 1
        
        return l 