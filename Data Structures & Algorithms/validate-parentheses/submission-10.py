class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', '}' : '{', ']': '['}
        q = []

        for ch in s:
            if ch in bracket_map:
                if q and bracket_map[ch] == q[-1]:
                    q.pop()
                else:
                    return False
            else:
                q.append(ch)
        return len(q) == 0
        