class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        stack = []
        result = []

        def backtrack(openP, closedP):
            if openP == closedP == n:
                result.append("".join(stack))
                return
            
            if openP < n:
                stack.append('(')
                backtrack(openP+1, closedP)
                stack.pop()
            
            if closedP < openP:
                stack.append(')')
                backtrack(openP, closedP+1)
                stack.pop()
            
        backtrack(0,0)    
        return result