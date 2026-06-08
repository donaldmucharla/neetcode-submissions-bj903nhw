from typing import List
import collections

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p1 = find(x)
            p2 = find(y)

            if p1 == p2:
                return

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

        emailToAccount = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i

        merged = collections.defaultdict(list)

        for email, i in emailToAccount.items():
            root = find(i)
            merged[root].append(email)

        res = []

        for i, emails in merged.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))

        return res