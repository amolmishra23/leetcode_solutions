# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth, height = Counter(), Counter()
        
        def preorder(node, d):
            if not node: return -1
            depth[node.val] = d
            curr = max(preorder(node.left, d+1), preorder(node.right, d+1))+1
            height[node.val] = curr
            return curr
        preorder(root, 0)
        
        cousins = defaultdict(list)
        
        for val, d in depth.items():
            cousins[d].append((height[val], val))
            cousins[d].sort(reverse=True)
            if len(cousins[d]) > 2: cousins[d].pop()
        
        res = []
        for q in queries:
            # "d" => Depth at this node
            # find the next best cousin at this level
            # find its height
            # thats the answer in this level
            d = depth[q]
            # if no cousin, we are the last child
            # so height of tree would be (d-1)
            if len(cousins[d])==1:
                res.append(d - 1)
            elif cousins[d][0][1] == q:
                res.append(d + cousins[d][1][0])
            else:
                res.append(d + cousins[d][0][0])
                
        return res