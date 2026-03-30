class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        visited = set()
        component = 0


        

        def bfs(node):
            stack = [node]

            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                
                visited.add(cur)

                for nei in adj[cur]:
                    if nei not in visited:
                        stack.append(nei)

        for n in range(n):
            if n not in visited:
                component += 1
                bfs(n) 
        
        return component

        