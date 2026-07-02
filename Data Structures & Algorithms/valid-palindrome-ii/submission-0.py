class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPlaindrome(left,right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
        
        l = 0
        r = len(s)-1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return (isPlaindrome(l+1, r) or isPlaindrome(l, r-1))
        return True
                        