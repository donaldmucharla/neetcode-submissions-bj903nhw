class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Add original index to each edge
        for i, edge in enumerate(edges):
            edge.append(i)

        # Sort by weight
        edges.sort(key=lambda x: x[2])

        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [1] * n

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)

                if pa == pb:
                    return False

                if self.rank[pa] > self.rank[pb]:
                    self.parent[pb] = pa
                    self.rank[pa] += self.rank[pb]
                else:
                    self.parent[pa] = pb
                    self.rank[pb] += self.rank[pa]

                return True

        def kruskal(skip_edge=None, force_edge=None):
            dsu = DSU(n)
            weight = 0
            count = 0

            # Force include one edge first
            if force_edge:
                u, v, w, idx = force_edge
                if dsu.union(u, v):
                    weight += w
                    count += 1

            for edge in edges:
                u, v, w, idx = edge

                if skip_edge is not None and idx == skip_edge:
                    continue

                if dsu.union(u, v):
                    weight += w
                    count += 1

            # MST must have n - 1 edges
            if count != n - 1:
                return float("inf")

            return weight

        mst_weight = kruskal()

        critical = []
        pseudo = []

        for edge in edges:
            u, v, w, idx = edge

            # Case 1: remove this edge
            # If MST weight increases, edge is critical
            if kruskal(skip_edge=idx) > mst_weight:
                critical.append(idx)

            # Case 2: force this edge
            # If MST weight stays same, edge is pseudo-critical
            elif kruskal(force_edge=edge) == mst_weight:
                pseudo.append(idx)

        return [critical, pseudo]