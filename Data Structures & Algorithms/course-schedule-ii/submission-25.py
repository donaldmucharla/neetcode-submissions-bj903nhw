class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)

        visiting = set()
        visited = set()
        res = []
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            visited.add(course)
            visiting.remove(course)
            res.append(course)
            return True
        for a in adj:
            if not dfs(a):
                return []
        
        return res