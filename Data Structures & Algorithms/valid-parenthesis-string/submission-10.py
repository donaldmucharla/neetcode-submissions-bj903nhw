class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(i, open_index):
            if open_index < 0:
                return False
            if i == len(s):
                return open_index == 0
            if (i, open_index) in memo:
                return memo[(i, open_index)]

            if s[i] == '(':
                ans = dfs(i + 1, open_index + 1)
            elif s[i] == ')':
                ans  = dfs(i + 1, open_index - 1)
            else:
                ans  = (dfs(i + 1, open_index) or
                        dfs(i + 1, open_index + 1) or
                        dfs(i + 1, open_index - 1))
            memo[(i, open_index)] = ans
            return ans
        return dfs(0, 0)