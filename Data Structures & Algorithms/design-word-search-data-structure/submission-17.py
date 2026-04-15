class TrieNode:
    def __init__(self):
        self.children  = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        
    def search(self, word: str) -> bool:
        def dfs(j , root):
            cur = root
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if not word[i] in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.isEnd
        return dfs(0, self.root)

        
