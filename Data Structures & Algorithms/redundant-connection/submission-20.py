class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent =[]
        for i in range(len(edges)+1):
            parent.append(i)
        
        rank = [1] * (len(edges)+1)

        def findParent(node):
            if node != parent[node]:
                parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1 = findParent(n1)
            p2 = findParent(n2)

            if p1 == p2:
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
        
        return []
