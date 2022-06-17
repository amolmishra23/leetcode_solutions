# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # global result. 
        self.res = 0
        
        def dfs(root):
            # just to handle special case of leaf nodes, where we dont want them to have camera, so return 2. 
            # now leaf can return 0, and leaf's parent would have the camera. 
            if not root: return 2
            
            # finding the situation with our children, if they need camera or not. 
            l, r = dfs(root.left), dfs(root.right)
            
            # if any child nodes not covered, mandatory to add camera
            if l==0 or r==0:
                self.res += 1
                return 1
            
            # if we reached here, means our child nodes were covered.
            # they can be themselves camera, or their kid has camera. 
            # if they have camera(l==1 or r==1), we can return 2 saying we dont need camera to our parent
            # if they dont have camera(l==2 and r==2), we need to return 0 to our parent, who mandatorily needs to have camera to cover us
            return 2 if l==1 or r==1 else 0
        
        # if dfs(root) returned 0 means its expected to be covered. So add 1 camera here as well. 
        return (dfs(root)==0) + self.res