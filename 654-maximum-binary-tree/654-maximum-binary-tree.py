# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def get_max(arr, start, end):
            max_, idx=float('-inf'), 0
            
            for i in range(start, end+1):
                if arr[i]>max_:
                    max_ = arr[i]
                    idx = i
                    
            return max_, idx
        
        def solve(nums, start, end):
            if start>end: return None
            
            if start==end: return TreeNode(nums[start])
            
            max_, idx = get_max(nums, start, end)
            node = TreeNode(nums[idx])
            node.left = solve(nums, start, idx-1)
            node.right = solve(nums, idx+1, end)
            
            return node
        
        return solve(nums, 0, len(nums)-1)