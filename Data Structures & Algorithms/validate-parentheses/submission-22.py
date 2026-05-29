class Solution:
    def isValid(self, s: str) -> bool:
        Bracket_map = {")" : "(", "]":"[", "}":"{"}
        q = []

        for c in s:
            if c in Bracket_map:
                if q and Bracket_map[c] == q[-1]:
                    q.pop()
                else:
                    return False  
            else:
                q.append(c)
        
        return True if len(q) == 0 else False
        