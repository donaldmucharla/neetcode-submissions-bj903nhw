class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}

        for cur, pre in prerequisites:
            preReq[cur].append(pre)
        visited = set()
        
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