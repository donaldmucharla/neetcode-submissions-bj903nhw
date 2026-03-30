class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = {i : [] for i in range(numCourses)}
        for cour, prev  in prerequisites:
            pre[cour].append(prev)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if pre[course] == []:
                return True
            
            visited.add(course)
            for prevq in pre[course]:
                if not dfs(prevq):
                    return False
            
            visited.remove(course)
            pre[course] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True        