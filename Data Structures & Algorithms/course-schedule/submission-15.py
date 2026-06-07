class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            visited.remove(course)
            adj[course] = []
            return True

        
        for a in adj:
            if not dfs(a):
                return False
        
        return True