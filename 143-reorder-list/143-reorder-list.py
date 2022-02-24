# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def print_ll(head):
            temp = head
            while temp:
                print (temp.val, end=" ")
                temp = temp.next
            print("")
            
        def find_middle(head):
            slow, fast = head, head
            
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def reverse_ll(head):
            curr = head
            prev, next_ = None, None
            
            while curr:
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
                
            return prev
        
        middle = find_middle(head)
        ll_b = reverse_ll(middle)
        ll_a = head
        
        while ll_a is not None and ll_b is not None:
            next_ = ll_a.next
            ll_a.next = ll_b
            ll_a = next_
            
            next_ = ll_b.next
            ll_b.next = ll_a
            ll_b = next_
            
        if ll_a is not None: ll_a.next=None
            
        return head
        