class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        memo = {}
        adj = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        res = []
        def dfs(src, target):
            if src == target:
                return True
            
            if (src, target) in memo:
                return memo[(src, target)]
            for nei in adj[src]:
                if dfs(nei, target):
                    memo[(src, target)] = True
                    return True
            memo[(src, target)] = False
            return False
        for a, b in queries:
            res.append(dfs(a, b))
        return res