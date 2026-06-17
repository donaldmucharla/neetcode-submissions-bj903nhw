class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res= []

        def dfs(openCount, closedCount, stack):
            if openCount == closedCount == n:
                res.append("".join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                dfs(openCount+1, closedCount, stack)
                stack.pop()
            
            if closedCount < openCount:
                stack.append(")")
                dfs(openCount, closedCount+1, stack)
                stack.pop()
        dfs(0, 0, [])
        return res