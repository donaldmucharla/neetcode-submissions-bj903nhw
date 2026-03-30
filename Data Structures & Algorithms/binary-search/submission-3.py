class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Calculate the middle index
            mid = ((l +r) // 2)
            
            if nums[mid] > target:
                # Target is in the left half
                r = mid - 1
            elif nums[mid] < target:
                # Target is in the right half
                l = mid + 1
            else:
                # Found the target
                return mid
                
        return -1