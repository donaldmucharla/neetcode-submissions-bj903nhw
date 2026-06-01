class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        a = ord('a')

        for c in s:
            freq[ord(c)-a] += 1
        
        for c in t:
            freq[ord(c)-a] -= 1
            if freq[ord(c)-a] < 0:
                return False
        
        return True 