class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_window = [0] * 26
        s2_window = [0] * 26

        for i in range(len(s1)):
            s1_window[ord(s1[i]) - ord('a')] += 1
            s2_window[ord(s2[i]) - ord('a')] += 1
        
        if s1_window == s2_window:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
            s2_window[ord(s2[r]) - ord('a')] += 1
            s2_window[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s2_window == s1_window:
                return True
        
        return False
