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
        
        # contains the union-find mappings of the emails
        ownership={}
        
        """
        In simple words, it contains the mapping of email to idx where it occured
        In addition for common emails, we also end up doing union find.
        So we know, 1 idx also belongs to 0 idx. 
        """
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])            
                ownership[email]=i
                
        ans = defaultdict(list)
        
        """
        Merging our inferences from union find. 
        """
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
            
        return [
            [accounts[i][0]] + sorted(emails) for i, emails in ans.items()
        ]