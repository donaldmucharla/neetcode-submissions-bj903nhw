class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visited = set()
        components = 0

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(i):
            visited.add(i)
            for x in adj[i]:
                if x not in visited:
                    dfs(x)
        
        for c in range(n):
            if c not in visited:
                dfs(c)
                components += 1
        
        return components
        