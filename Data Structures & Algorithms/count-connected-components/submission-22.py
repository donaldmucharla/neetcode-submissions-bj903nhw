class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0

        for a in adj:
            if a not in visited:
                dfs(a)
                count += 1
        
        return count
