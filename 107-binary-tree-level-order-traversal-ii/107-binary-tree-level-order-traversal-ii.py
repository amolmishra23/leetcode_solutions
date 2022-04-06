from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        q = deque([root])
        res = []
        while q:
            len_ = len(q)
            temp = []
            for _ in range(len_):
                front = q.popleft()
                temp.append(front.val)
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            res.append(temp)
            
        return res[::-1]