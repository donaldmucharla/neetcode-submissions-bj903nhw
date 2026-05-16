class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {i:[] for i, j in tickets}
        tickets.sort()
        for x, y in tickets:
            adj[x].append(y)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == (len(tickets)+1):
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])

            for i, j in enumerate(temp):
                dest = adj[src].pop(i)
                res.append(dest)
                if dfs(dest):
                    return True
                adj[src].insert(i, dest)
                res.pop()
            return False
        
        dfs("JFK")
        return res
                

