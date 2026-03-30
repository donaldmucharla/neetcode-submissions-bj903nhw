class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {} #(value, index)

        for i, n in enumerate(nums):
            differance = target - n
            if differance in diff:
                return [diff[differance], i]
            diff[n] = i 

        