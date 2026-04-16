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
        for word in words:
            root.addWord((word))
        ROW, COL = len(board), len(board[0])
        res = set()
        visited = set()
        def dfs(r, c, word, node):
            if (r<0) or c<0 or r >= ROW or c >= COL or board[r][c] not in node.children or (r, c) in visited:
                return
            visited.add((r, c))
            word = word+board[r][c]
            node = node.children[board[r][c]]
            if node.isEnd:
                res.add(word)
            
            dfs(r, c+1, word, node)
            dfs(r+1, c, word, node)
            dfs(r-1, c, word, node)
            dfs(r, c-1, word, node)

            visited.remove((r, c))
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, "", root)
        
        return list(res)



        