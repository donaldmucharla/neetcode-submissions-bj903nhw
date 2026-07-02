class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        ans = ""
        for i in range(minLen):
            ans = ans + word1[i] + word2[i]
        
        if len(word1) > minLen:
            ans = ans + word1[minLen :]
        if len(word2) > minLen:
            ans = ans + word2[minLen :]
        return ans