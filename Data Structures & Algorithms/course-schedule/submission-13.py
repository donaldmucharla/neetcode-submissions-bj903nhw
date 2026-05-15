class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = { i:[] for i in range(numCourses) }

        for c, p in prerequisites:
            preReqMap[c].append(p)
        
        visited = set()
        
        def dfs(cur):
            if cur in visited:
                return False
            
            if preReqMap[cur] == []:
                return True
            
            visited.add(cur)
            for c in preReqMap[cur]:
                if not dfs(c):
                    return False
            
            visited.remove(cur)
            preReqMap[cur] = []

            return True
        

        for p in preReqMap:
            if not dfs(p):
                return False
        
        return True
            


