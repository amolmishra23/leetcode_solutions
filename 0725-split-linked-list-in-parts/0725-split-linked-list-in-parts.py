# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:        
        def listLength(head):
            l = 0
            while head:
                head = head.next; l += 1
            return l
        
        l = listLength(head)
        q, r = divmod(l, k)
        res = []
        
        while head:
            curr_size = q
            if r: 
                curr_size+=1; r-=1
            
            res.append(head)
            
            for _ in range(curr_size-1):
                head = head.next
                
            if head == None: break
            head.next, head = None, head.next
            
        while len(res)<k: res.append(None)
            
        return res