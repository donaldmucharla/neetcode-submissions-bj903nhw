class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = collections.defaultdict(int)

        for n in nums:
            freq[n] += 1
        target = len(nums)//3
        res = []
        for n, count in freq.items():
            if count > target:
                res.append(n)
        return res
