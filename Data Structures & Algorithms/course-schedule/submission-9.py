class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {course:[] for course in range(numCourses)}
        visited = set()

        for cur, pre in prerequisites:
            preReq[cur].append(pre)
        
        def dfs(cur):
            if cur in visited:
                return False
            if preReq[cur] == []:
                return True
            
            visited.add(cur)

            for pre in preReq[cur]:
                if not dfs(pre):
                    return False
            
            visited.remove(cur)
            preReq[cur] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        