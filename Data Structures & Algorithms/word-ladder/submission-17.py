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
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)
        res =1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for p in nei[pattern]:
                        if not p in visited:
                            q.append(p)
                            visited.add(p)
            res += 1
        
        return 0
                
