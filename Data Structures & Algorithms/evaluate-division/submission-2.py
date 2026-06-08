class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        def dfs(src, target, visited):
            if src not in graph:
                return -1.0
            if src == target:
                return 1.0
            
            visited.add(src)
            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei, target, visited)

                    if res != -1.0:
                        return res * weight
            
            return -1.0
        
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        
        return res
