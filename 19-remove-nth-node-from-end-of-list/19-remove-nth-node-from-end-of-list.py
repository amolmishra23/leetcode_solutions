# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
            