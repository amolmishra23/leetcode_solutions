class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, a):
        if a!=self.parents[a]:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]
    
    def union(self, a, b):
        self.parents[self.find(a)] = self.find(b)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        owner = {}
        
        # 1. try to find the graph relations using previously occured email.
        # and add them in the union find. 
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in owner:
                    uf.union(i, owner[email])
                else:
                    owner[email] = i
                
        ans = defaultdict(list)
        
        # Now create a map of owner to email. 
        # this could be done using union-find, and add similar emails in the owner to email. 
        for email, o in owner.items():
            ans[uf.find(o)].append(email)
            
        # finally, we make the result list, where 1st element is owner name, and rest entries are owner emails(which we figured using union-find)
        return [
            [accounts[i][0]] + sorted(emails) for i, emails in ans.items()
        ]
                