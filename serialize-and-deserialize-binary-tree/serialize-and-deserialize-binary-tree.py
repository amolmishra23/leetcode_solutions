# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def solve(root, res):
            if root is None: res.append("X"); return
            
            res.append(root.val)
            solve(root.left, res)
            solve(root.right, res)
            
        res = []
        solve(root, res)
        print(res)
        return res
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def solve(data):
            if len(data)==0: return None
            
            root = data.pop(0)
            if root=="X": return None
            
            node = TreeNode(root)
            node.left = solve(data)
            node.right = solve(data)
            return node
        
        return solve(data)
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))