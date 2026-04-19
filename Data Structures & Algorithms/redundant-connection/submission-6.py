class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)

        def find(n):
            if n != parent[n]:
                return find(parent[n])
            return parent[n]

        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            if p1==p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
