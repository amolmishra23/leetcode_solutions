# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        
        def traverse(root):
            while root:
                yield root.val
                root = root.next
            while True: yield -1
        t = traverse(head)
        
        top, bottom = 0, m-1
        left, right = 0, n-1
        
        while left<=right and top<=bottom:
            for i in range(left, right+1):
                res[top][i] = next(t)
            top += 1
            
            for i in range(top, bottom+1):
                res[i][right] = next(t)
            right -=1
            
            if top<=bottom:
                for i in range(right, left-1, -1):
                    res[bottom][i] = next(t)
            bottom -= 1
            
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res[i][left] = next(t)
            left += 1
            
        return res
    
        