class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Bracket_map = { ")":"(", "}":"{", "]":"["}


        for c in s:
            if c in Bracket_map:
                if stack and stack[-1] == Bracket_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
        