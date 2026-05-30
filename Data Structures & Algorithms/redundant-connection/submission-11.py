class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i  in range(n+1)]
        rank = [1] * (n+1)

        def findParent(p):
            if p != parent[p]:
                return findParent(parent[p])
            return parent[p]

        
        def union(x, y):
            p1 = findParent(x)
            p2 = findParent(y)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]
            return True
        for x, y in edges:
            if not union(x, y):
                return [x, y]
        return []
