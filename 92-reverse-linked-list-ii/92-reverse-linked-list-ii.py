# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        def rev_list(curr, k):
            prev, tail = None, curr
            
            for _ in range(k):
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
                
            # we are returning new_curr, new_head, new_tail here respectively
            return curr, prev, tail
        
        k = n-m+1
        prev, curr = None, head
        while m>1:
            prev = curr
            curr = curr.next
            m-=1
            
        new_curr, new_head, new_tail = rev_list(curr, k)
        if prev: prev.next = new_head
        new_tail.next = new_curr
        
        return head if prev else new_head
    