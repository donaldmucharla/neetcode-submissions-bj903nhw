class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def findP(n):
            if parent[n] != n:
                return findP(parent[n])
            return parent[n]


        def union(n1, n2):
            p1 = findP(n1)
            p2 = findP(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
            else:
                parent[p2] = parent[p1]
                rank[p2] += rank[p1]
            return True
            
        for x, y in edges:
            if not union(x, y):
                return [x, y]