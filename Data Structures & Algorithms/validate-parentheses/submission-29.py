class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for ch in s:
            if ch in bracket:
                if not stack or stack[-1] != bracket[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return True if len(stack) == 0 else False
                
            
