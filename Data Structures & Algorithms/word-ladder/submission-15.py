class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        visited = set()
        visited.add(beginWord)
        q =collections.deque()
        q.append(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
            
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in nei[pattern]:
                        if not neighbor in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            
            res += 1
        
        return 0
        