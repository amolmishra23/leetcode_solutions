# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def find_middle(head):
            slow, fast = head, head
            
            while fast is not None and fast.next is not None:
                slow=slow.next
                fast=fast.next.next
                
            return slow
        
        def reverse(head):
            curr=head
            prev,next_ = None, None
            
            while curr:
                next_=curr.next
                curr.next = prev
                prev = curr
                curr = next_
                
            return prev
        
        middle = find_middle(head)
        rev_ll = reverse(middle)
        ll_a = head
        ll_b = rev_ll
        
        while ll_a is not None and ll_b is not None:
            if ll_a.val != ll_b.val: break
            ll_a = ll_a.next
            ll_b = ll_b.next
            
        reverse(ll_b)
        
        if ll_a is None or ll_b is None: return True
        
        return False