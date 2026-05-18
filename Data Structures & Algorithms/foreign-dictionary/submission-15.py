class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c : set() for word in words for c in word}

        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i+1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []
        
        def dfs(w):
            if w in visited:
                return visited[w]
            
            visited[w] = True

            for nei in adj[w]:
                if dfs(nei):
                    return True
            
            res.append(w)
            visited[w] =  False
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
        