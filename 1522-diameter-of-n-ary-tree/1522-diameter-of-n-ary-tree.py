class Solution:
    def diameter(self, root: 'Node') -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, root):
        first = second = 0  # base case for leaf, first store the maximum depth, second is second maximum depth
        for neighbor in root.children:
            depth = self.dfs(neighbor)
            if depth > first:
                first, second = depth, first
            elif depth > second:
                second = depth
        self.diameter = max(self.diameter, first + second)
        return first + 1