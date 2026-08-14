class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            lenght = len(s)
            res += str(lenght) + "#" + s

        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1

            lenght = int(s[l:r])
            start = r+1
            end = start + lenght
            res.append(s[start:end])
            l = end

        return res



