class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        n = len(nums) 
        left_arr = [1] * n
        for l in range(n):
            left_arr[l] = left
            left = left * nums[l]
        

        right = 1
        right_arr = [1] * n
        for r in range(n-1, -1, -1):
            right_arr[r] = right
            right = right * nums[r]

        output = [1] * n
        for o in range(n):
            output[o] = left_arr[o] * right_arr[o]

        return output 

        