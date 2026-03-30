class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        adj = {i:[] for i in range(n)}

        visited = set()
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visited)
        