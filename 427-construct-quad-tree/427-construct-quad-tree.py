"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def is_leaf(self, grid, top_row, top_col, bottom_row, bottom_col):
        return all(grid[top_row][top_col] == grid[i][j] for i in range(top_row, bottom_row) for j in range(top_col, bottom_col))
        
    def build(self, grid, top_row, top_col, bottom_row, bottom_col):
        if self.is_leaf(grid, top_row, top_col, bottom_row, bottom_col):
            return Node(grid[top_row][top_col]==1, True, None, None, None, None)
        
        mid_row = top_row + (bottom_row-top_row)//2
        mid_col = top_col + (bottom_col-top_col)//2
        
        top_left = self.build(grid, top_row, top_col, mid_row, mid_col)
        top_right = self.build(grid, top_row, mid_col, mid_row, bottom_col)
        bottom_left = self.build(grid,mid_row, top_col, bottom_row, mid_col)
        bottom_right = self.build(grid,mid_row, mid_col, bottom_row, bottom_col)
        
        return Node(None, False, top_left, top_right, bottom_left, bottom_right)
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.build(grid, 0, 0, n, n)