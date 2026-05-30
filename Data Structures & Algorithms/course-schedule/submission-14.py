class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_Map = {i:[] for i in range(numCourses)}

        for cour, pre in prerequisites:
            adj_Map[cour].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if adj_Map[course] == []:
                return True
            
            visited.add(course)
            for neig in adj_Map[course]:
                if not dfs(neig):
                    return False
            
            visited.remove(course)
            adj_Map[course] = []
            return True
        for a in adj_Map:
            if not dfs(a):
                return False
        
        return True




