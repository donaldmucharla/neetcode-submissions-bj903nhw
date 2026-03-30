from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(t_count)
        res = [-1, -1]
        res_len = float('inf')

        l = 0
        for r, ch in enumerate(s):
            window[ch] += 1
            # Correct: check if ch is required and counts match
            if ch in t_count and window[ch] == t_count[ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                # Correct: remove character going out of the window (s[l])
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
