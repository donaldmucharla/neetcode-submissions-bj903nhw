class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closedN, stack):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                dfs(openN+1, closedN, stack)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN+1, stack)
                stack.pop()
            
        dfs(0, 0, [])
        return res

        