# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head = ListNode(None), ListNode(None)
        odd_copy, even_copy = odd_head, even_head
        odd_turn = True
        
        while (head):
            if odd_turn:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                even_head.next = head
                even_head = even_head.next
            head = head.next
            odd_turn = not odd_turn
            
        odd_head.next = even_copy.next
        even_head.next = None
        return odd_copy.next