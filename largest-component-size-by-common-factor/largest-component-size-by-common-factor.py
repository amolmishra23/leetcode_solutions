class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        
    def find(self, i):
        if self.parents[i]==i: return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p==root_q: return
        small, big = sorted([root_p, root_q], key = lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        In order to find the prime factors, we basically check from number to its sqrt+1
        Then we do union of number, with all its factors. 
        Then find the size of each component. 
        We need to return result as the size of the biggest component.
        """
        uf = UnionFind(100001)
        
        for x in A:
            for i in range(2, int(sqrt(x))+1):
                if x%i==0:
                    uf.union(x, i)
                    uf.union(x, x//i)
                    
        counter = Counter()
        
        for num in A:
            root = uf.find(num)
            counter[root]+=1
        
        return max(counter.values())