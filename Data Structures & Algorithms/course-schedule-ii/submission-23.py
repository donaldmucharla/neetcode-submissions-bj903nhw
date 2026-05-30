class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacent_map = {i : [] for i in range(numCourses)}
        visited1  = set()
        visited2 = set()
        res = []
        for cur, pre in prerequisites:
            adjacent_map[cur].append(pre)

        def dfs(cur):
            if cur in visited1:
                return False
            if cur in visited2:
                return True
            
            visited1.add(cur)
            for nei in adjacent_map[cur]:
                if not dfs(nei):
                    return False

            visited1.remove(cur)
            visited2.add(cur)
            res.append(cur)
            return True
        for a in adjacent_map:
            if not dfs(a):
                return []
        
        return res
