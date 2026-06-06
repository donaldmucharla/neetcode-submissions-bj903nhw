class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = collections.defaultdict()

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        maxk = 0
        ans = nums[0]
        for i,f in freq.items():
            if maxk < f:
                maxk = f
                ans = i
        return ans
