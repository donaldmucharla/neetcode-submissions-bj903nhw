class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)

        memo = {}

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

        ans = []
        for u, v in queries:
            ans.append(dfs(u, v))

        return ans