class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        res = []

        freq_list = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        for r in range(k):
            res.append(freq_list[r][0])
        return res