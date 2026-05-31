class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for word in words for c in word}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        visited1 = set()
        visited2 = set()

        res = []

        def dfs(c):
            if c in visited1:
                return False
            if c in visited2:
                return True
            
            visited1.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            visited1.remove(c)
            res.append(c)
            visited2.add(c)
            return True
        for c in adj:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
