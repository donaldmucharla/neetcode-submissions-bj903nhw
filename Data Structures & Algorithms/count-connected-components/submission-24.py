class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        count = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        for a in adj:
            if a not in visited:
                dfs(a)
                count += 1
        
        return count
