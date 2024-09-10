# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        if b==0: return a
        return self.gcd(b, a%b)
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headCopy = head
        
        while head and head.next:
            curr_val = head.val
            next_val = head.next.val
            new_node = ListNode(self.gcd(curr_val, next_val), head.next)
            head.next = new_node
            head = new_node.next
            
        return headCopy
        