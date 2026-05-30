class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openCount, closeCount, cur):
            if len(cur) == n*2:
                res.append(cur)
                return
            
            if openCount < n:
                dfs(openCount +1, closeCount, cur+"(")
            if closeCount < openCount:
                dfs(openCount, closeCount+1, cur +")")
        
        dfs(0, 0, "")
        return res