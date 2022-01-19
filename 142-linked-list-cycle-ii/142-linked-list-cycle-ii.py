# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            # using LL algo to find cycle
            slow = slow.next
            fast = fast.next.next
            if slow==fast: break
        else:
            # there is no cycle for sure, and we have reached end of iteration. 
            return None
        
        while head!=slow:
            head = head.next
            slow = slow.next
            
        return head