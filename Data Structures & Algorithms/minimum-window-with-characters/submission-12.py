class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        res = [-1, -1]
        resLen = float("inf")
        l = 0

        window = {}

        count = collections.Counter(t)
        have, need = 0, len(count)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c, 0)
            if c in count and window[c] == count[c]:
                have += 1
            
            while have ==  need:
                if resLen > (r - l +1):
                    resLen = (r - l + 1)
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in count and  window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""







