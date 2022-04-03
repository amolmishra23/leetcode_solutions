class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.size[px] < self.size[py]:
            self.parent[px] = self.parent[py]
            self.size[py] += self.size[px]
        else:
            self.parent[py] = self.parent[px]
            self.size[px] += self.size[py]
            
        return True


class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        # Union find
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y: return 0
            root[x] = y
            return 1

        res = e1 = e2 = 0

        # Alice and Bob
        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if uni(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = root[:]

        # only Alice
        for t, i, j in edges:
            if t == 1:
                if uni(i, j):
                    e1 += 1
                else:
                    res += 1

        # only Bob
        root = root0
        for t, i, j in edges:
            if t == 2:
                if uni(i, j):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1