class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : [] for word in words for c in word}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        visiting = set()
        visited = set()
        res = []

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            
            visiting.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visited.add(c)
            visiting.remove(c)
            res.append(c)

            return True
        for a in adj:
            if not dfs(a):
                return ""
        res = res[::-1]
        return "".join(res)
                