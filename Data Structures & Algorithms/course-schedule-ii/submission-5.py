class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        
        res = []
        visited = set()
        circle = set()

        def dfs(course):
            if course in circle:
                return False
            if course in visited:
                return True
            circle.add(course)
            for pre in preReq[course]:
                if dfs(pre) == False:
                    return False
            circle.remove(course)
            visited.add(course)
            res.append(course)
            return True
            

        

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res

        