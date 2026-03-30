from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        used = [False] * len(strs)
        res = []

        for i in range(len(strs)):
            if used[i]:
                continue
            
            group = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True

            res.append(group)

        return res