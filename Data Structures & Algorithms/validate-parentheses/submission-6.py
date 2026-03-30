class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { ")": "(", "}":"{", "]" : "["}
        stack = []

        for c in s:
            if c in bracket_map:
                top_bracket  = stack.pop() if stack else "#"
                if top_bracket != bracket_map[c]:
                    return False
            
            else:
                stack.append(c)
        
        return not stack