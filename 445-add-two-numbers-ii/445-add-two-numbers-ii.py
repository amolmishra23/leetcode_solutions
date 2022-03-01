# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            if not head or not head.next: return head
            
            prev, curr = None, head
            
            while curr:
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
            return prev
        
        def add(l1, l2):
            carry = 0
            ret = curr = ListNode(None)
            
            while l1 or l2 or carry:
                if l1:
                    carry += l1.val
                    l1 = l1.next
                if l2:
                    carry += l2.val
                    l2 = l2.next
                
                q, r = divmod(carry, 10)
                curr.next = ListNode(r)
                curr = curr.next
                carry = q
            
            return ret.next
        
        l1, l2 = reverse(l1), reverse(l2)
        l3 = add(l1, l2)
        l3 = reverse(l3)
        return l3