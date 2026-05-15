class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}
        visited1 = set()
        visited2 = set()

        output = []

        for c, p in prerequisites:
            preReq[c].append(p)
        
        def dfs(cur):
            if cur in visited1:
                return False
            
            if cur in visited2:
                return True
            
            visited1.add(cur)

            for p in preReq[cur]:
                if not dfs(p):
                    return False
            
            visited1.remove(cur)
            visited2.add(cur)
            output.append(cur)
            return True


        for p in preReq:
            if not dfs(p):
                return []
        
        return output
        