class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inward = [0] * (n+1)
        outward = [0] * (n+1)

        for i, o in trust:
            inward[i] += 1
            outward[o] += 1
        
        for i in range(1, n+1):
            if inward[i] == 0 and outward[i] == (n-1):
                return i
        
        return -1