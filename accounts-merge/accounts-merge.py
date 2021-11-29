class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, node):
        # we need to check if node is its own parent or not
        if node != self.parents[node]:
            # if its not parent, we set parent of node 
            self.parents[node] = self.find(self.parents[node])    
        # returning the actual parent
        return self.parents[node]
    
    def union(self, child, parent):
        # make the group of child node, have parent node as parent. 
        self.parents[self.find(child)] = self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
                
        ans = collections.defaultdict(list)
        
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
            
        return [[accounts[i][0]] + sorted(emails)  for i,emails in ans.items()]