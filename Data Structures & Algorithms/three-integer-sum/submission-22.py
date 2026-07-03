class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                totalSum = nums[i] + nums[left] + nums[right]

                if totalSum < 0:
                    left += 1
                elif totalSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
        return res
