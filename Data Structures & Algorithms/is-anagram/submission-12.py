class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        a_ord = ord('a')

        for i in s:
            freq[ord(i) - a_ord] += 1
        
        for j in t:
            freq[ord(j) - a_ord] -= 1
            if freq[ord(j) - a_ord] < 0:
                return False
        return True
        