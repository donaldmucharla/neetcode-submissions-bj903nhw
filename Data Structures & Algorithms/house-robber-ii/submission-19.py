class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(arr):
            rob1 = 0
            rob2 = 0
            for num in arr:
                tmp = max(rob2, rob1+num)
                rob1 = rob2
                rob2 = tmp
            
            return rob2
        
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))