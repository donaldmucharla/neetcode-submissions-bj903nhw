class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {course:[] for course in range(numCourses)}
        visited1 = set()
        visited2 = set()
        output = []

        for cur, pre in prerequisites:
            preReq[cur].append(pre)
        
        def dfs(cur):
            if cur in visited1:
                return False
            if cur in visited2:
                return True
            
            visited1.add(cur)

            for pre in preReq[cur]:
                if not dfs(pre):
                    return False
            
            visited1.remove(cur)
            visited2.add(cur)
            output.append(cur)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
        
        