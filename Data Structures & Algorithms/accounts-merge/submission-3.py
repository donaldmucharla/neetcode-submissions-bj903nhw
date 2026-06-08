class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def findParent(x):
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(n1, n2):
            p1 = findParent(n1)
            p2 = findParent(n2)

            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+= rank[p1]
            
        emailToAcc = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        merge = collections.defaultdict(list)

        for email, indx in emailToAcc.items():
            root = findParent(indx)
            merge[root].append(email)
        
        res = []
        for indx, emails in merge.items():
            name = accounts[indx][0]
            res.append([name]+sorted(emails))
        
        return res
