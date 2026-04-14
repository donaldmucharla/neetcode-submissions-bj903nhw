class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        