import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        res = []
        q = collections.deque()

        for i in range(n):
            # Remove indices that are out of the current window
            if q and q[0] == i - k:
                q.popleft()

            # Remove indices whose values are less than nums[i]
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Append the current index
            q.append(i)

            # If window is full, append current max to result
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
