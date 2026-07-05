class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res=  []
        q= collections.deque()

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if q[0] < l:
                q.popleft()
            
            if k <= (r-l+1):
                res.append(nums[q[0]])
                l += 1
            
        return res