class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        count = 0

        def dfs(i):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    dfs(j)

        for x in range(n):
            if x not in visited:
                dfs(x)
                count += 1
        
        return count

        