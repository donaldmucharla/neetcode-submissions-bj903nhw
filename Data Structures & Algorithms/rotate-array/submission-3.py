class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        t = k%n

        def reverseArr(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverseArr(0, n-1)
        reverseArr(0, t-1)
        reverseArr(t, n-1)