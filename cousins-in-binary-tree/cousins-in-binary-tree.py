# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None: return False
        q = deque()
        q.append(root)
        
        # performing a level order traversal to make sure cousins exist on the same level
        # even dfs can find the answer, but level order makes more sense
        while q:
            n = len(q)
            x_exist, y_exist = False, False
            
            # if within a level x and y exist, then we return True
            for i in range(n):
                curr = q.popleft()
                if curr.val == x: x_exist=True
                if curr.val == y: y_exist=True
                
                if curr.left and curr.right:
                    # because they are siblings
                    if curr.left.val in {x,y} and curr.right.val in {x,y}: return False
                    
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                    
            if x_exist and y_exist: return True
            
        return False
        