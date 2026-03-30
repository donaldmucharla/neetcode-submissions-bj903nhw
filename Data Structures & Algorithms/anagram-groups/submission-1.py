from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # Letter count for each character (26 lowercase letters)
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(word)
        return list(anagrams.values())
