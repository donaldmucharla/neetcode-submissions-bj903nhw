class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []
        def dfs(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(j+1, cur)
                    cur.pop()
        
        dfs(0, [])
        return res

    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
