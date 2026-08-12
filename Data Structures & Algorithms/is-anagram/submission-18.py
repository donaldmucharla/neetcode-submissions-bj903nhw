class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        a_ord  = ord('a')

        for i in range(len(s)):
            freq[ord(s[i]) - a_ord] += 1
        
        for i in range(len(t)):
            freq[ord(t[i]) - a_ord] -= 1
            if freq[ord(t[i]) - a_ord] < 0:
                return False
        
        return True