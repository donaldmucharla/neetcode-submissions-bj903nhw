class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        adj = [[] for _ in range(n)]
        for node, adjN in edges:
            adj[node].append(adjN)
            adj[adjN].append(node)
        visited = set()
        
        def dfs(n, prevN):
            if n in visited:
                return False

            visited.add(n)

            for i in adj[n]:
                if i == prevN:
                    continue
                if not dfs(i, n):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

            
            
        