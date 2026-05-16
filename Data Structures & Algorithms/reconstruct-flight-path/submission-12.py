class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {i:[] for i, j in tickets}
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
        
        res =  ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            
            if src not in adj:
                return False
            
            tmp = list(adj[src])
            for i, j in enumerate(tmp):
                s = adj[src].pop(i)
                res.append(s)
                if dfs(s):
                    return True
                adj[src].insert(i, s)
                res.pop()
            return False
        dfs("JFK")

        return res
            


        