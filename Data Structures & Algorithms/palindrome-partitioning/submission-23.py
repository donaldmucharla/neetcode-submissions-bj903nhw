class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, cur):
            if i >= len((s)):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(j+1, cur)
                    cur.pop()
        dfs(0, [])
        return res
    
    def isPalindrome(self, st, l, r):
        while l <= r:
            if st[l]!=st[r]:
                return False
            l += 1
            r -= 1
        return True