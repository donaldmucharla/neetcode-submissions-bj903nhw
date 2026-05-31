class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for s, d in tickets:
            adj[s].append(d)
        
        for src in adj:
            adj[src].sort(reverse=True)
        
        res = []

        def dfs(flight):
            while adj[flight]:
                next_flight = adj[flight].pop()
                dfs(next_flight)
            res.append(flight)
        dfs("JFK")
        return res[::-1]