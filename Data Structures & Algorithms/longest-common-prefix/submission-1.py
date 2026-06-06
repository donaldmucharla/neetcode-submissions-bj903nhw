class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]
        minLen =  min(len(first), len(last))
        res = ""

        for i in range(minLen):
            if first[i] != last[i]:
                return res
            res = res + first[i]
        
        return res
