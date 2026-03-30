class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        left_output = [1]*len(nums)

        for i in range(len(nums)):
            left_output[i] = left
            left *= nums[i]
        
        right = 1

        right_output = [1]*len(nums)

        for j in range(len(nums)-1, -1, -1):
            right_output[j] = right
            right *= nums[j]
        output = [1]*len(nums)
        for o in range(len(nums)):
            output[o] = left_output[o] * right_output[o]
        
        return output

        