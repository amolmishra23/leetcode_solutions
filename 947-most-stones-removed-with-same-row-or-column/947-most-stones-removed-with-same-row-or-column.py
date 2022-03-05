import collections

"""
We need to organize all the stones in components. 
Then difference of number of components, and total number of stones, is the largest number of moves we can make. 
"""
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        
    def find(self, i):
        if i==self.parents[i]: return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, p, q):
        root_p, root_q = map(self.find, (p, q))
        if root_p == root_q: return
        small, big = sorted([root_p, root_q], key = lambda x: self.sizes[x])
        self.parents[small]=big
        self.sizes[big]+=self.sizes[small]
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        MAX_ROWS = 10000
        uf = UnionFind(MAX_ROWS*2)
        
        for r, c in stones:
            uf.union(r, c+MAX_ROWS)
        
        return len(stones) - len({uf.find(r) for r, _ in stones})
        
        