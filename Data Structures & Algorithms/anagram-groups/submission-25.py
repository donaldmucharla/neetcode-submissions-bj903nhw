class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = collections.defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            
            count[tuple(freq)].append(s)
        
        return list(count.values())

        