# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = ListNode(None)
        copy_temp_node = temp_node
        carry = 0
        
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            carry, r = divmod(carry, 10)
            temp_node.next = ListNode(r)
            temp_node = temp_node.next
            
        if carry: temp_node.next = ListNode(carry)
        
        return copy_temp_node.next