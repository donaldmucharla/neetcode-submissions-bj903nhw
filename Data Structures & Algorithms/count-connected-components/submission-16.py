class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visited =set()
        components = 0

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        def dfs(i):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                     dfs(j)
        

        for a in adj:
            if a not in visited:
                dfs(a)
                components += 1
            
        return components

        