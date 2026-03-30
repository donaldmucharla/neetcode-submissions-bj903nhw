class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0]*26
        a_ord = ord('a')

        for c in s:
            freq[ord(c) - a_ord] += 1
        
        for c in t:
            freq[ord(c) - a_ord] -= 1
            if freq[ord(c) - a_ord] < 0:
                return False
        return True
        
        