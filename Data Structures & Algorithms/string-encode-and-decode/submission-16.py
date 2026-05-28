class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))+"#"+s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            
            start = j+1
            length = int(s[i:j])
            end = start + length

            res.append(s[start: end])
            i = start+length
        
        return res
