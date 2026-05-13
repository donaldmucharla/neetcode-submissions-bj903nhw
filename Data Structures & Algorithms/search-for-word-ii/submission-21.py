class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def addWord(self, word):
        cur = self
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.isEnd = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROW, COL = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, word, node):
            if node.isEnd:
                res.add(word)
            if (c < 0 or r < 0 or c >= COL or r >= ROW or (r, c) in visited or board[r][c] not in node.children):
                return

            visited.add((r, c))
            word = word + board[r][c]
            node = node.children[board[r][c]]

            dfs(r+1, c, word, node)
            dfs(r, c+1, word, node)
            dfs(r-1, c, word, node)
            dfs(r, c-1, word, node)
            visited.remove((r, c))
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, "", root)
        
        return list(res)
            
             
        


