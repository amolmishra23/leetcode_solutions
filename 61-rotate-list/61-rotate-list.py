# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        def ll_length(node):
            len_ = 0
            
            while node:
                node = node.next
                len_+=1
            
            return len_
        
        l = ll_length(head)
        
        if l <= 1: return head
        
        k = k%l if k>=l else k
        
        if k==0: return head
        
        slow, fast = head, head
        
        for _ in range(k):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        new_head = slow.next
        fast.next = head
        slow.next = None
        
        return new_head