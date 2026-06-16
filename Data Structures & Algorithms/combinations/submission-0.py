class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, curComb):
            if len(curComb) == k:
                res.append(curComb.copy())
                return
            
            if i > n:
                return
            
            curComb.append(i)
            dfs(i+1, curComb)
            curComb.pop()
            dfs(i+1, curComb)
        
        dfs(1, [])
        return res
