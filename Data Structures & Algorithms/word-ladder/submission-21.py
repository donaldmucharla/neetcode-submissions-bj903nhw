class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(list)
        if not endWord in wordList:
            return 0

        if not beginWord in wordList:
            wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" +word[i+1:]
                adj[pattern].append(word)
        
        count = 1
        visited = set([beginWord])
        q = collections.deque([beginWord])

        while q:
            n = len(q)
            for i in range(n):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            count += 1
        
        return 0

        