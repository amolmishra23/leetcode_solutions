# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(node):
            if node is None or node.next is None: return None
            prev, slow, fast = node, node, node
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
                
            prev.next = prev.next.next
            return node
        
        return solve(head)
            