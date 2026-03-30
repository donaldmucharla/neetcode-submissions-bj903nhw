class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_counter = collections.Counter(s1)

        n = len(s1)

        for i in range(len(s2)-n+1):
            window = s2[i:i+n]
            if collections.Counter(window) == s1_counter:
                return True
        
        return False
        