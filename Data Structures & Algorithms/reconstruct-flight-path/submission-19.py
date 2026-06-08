class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        
        for src in adj:
            adj[src].sort(reverse = True)
        
        res = []

        def dfs(src):
            while adj[src]:
                next_scr = adj[src].pop()
                dfs(next_scr)
            res.append(src)
        dfs("JFK")
        return res[::-1]