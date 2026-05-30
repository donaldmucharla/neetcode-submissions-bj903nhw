class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count, close_count, current_str):
            # Base Case: Valid combination found
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Rule 1: We can add an opening bracket if we haven't reached the limit n
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Rule 2: We can add a closing bracket if it doesn't exceed open brackets
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return res