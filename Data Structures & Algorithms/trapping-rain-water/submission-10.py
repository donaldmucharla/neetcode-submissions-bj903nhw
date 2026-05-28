class Solution:
    def trap(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        leftMax = 0
        rightMax = 0

        res = 0

        while left < right:

            if arr[left] < arr[right]:

                leftMax = max(leftMax, arr[left])

                res += leftMax - arr[left]

                left += 1

            else:

                rightMax = max(rightMax, arr[right])

                res += rightMax - arr[right]

                right -= 1

        return res
        