class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        s1_freq = [0] * 26

        for s in s1:
            s1_freq[ord(s)- ord('a')] += 1
        window_freq = [0] * 26

        l = 0

        for r in range(len(s2)):
            window_freq[ord(s2[r]) - ord('a')] += 1

            while len(s1) < (r - l+1):
                window_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s1_freq == window_freq:
                return True
        
        return False

