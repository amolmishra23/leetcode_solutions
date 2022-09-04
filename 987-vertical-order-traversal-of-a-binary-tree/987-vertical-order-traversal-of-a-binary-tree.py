# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, q = defaultdict(list), deque()
        q.append((root, 0))
        
        while q:
            temp = defaultdict(list)
            for _ in range(len(q)):
                node, level = q.popleft()
                temp[level].append(node.val)
                if node.left: q.append([node.left, level-1])
                if node.right: q.append([node.right, level+1])
            for key in temp: res[key].extend(sorted(temp[key]))
        
        return [res[i] for i in sorted(res)]
        