class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i, o in enumerate(order):
            rank[o] = i
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if w1.startswith(w2) and len(w1) > len(w2):
                return False
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
        
        return True