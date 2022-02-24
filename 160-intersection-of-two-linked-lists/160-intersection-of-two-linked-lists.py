# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Extremely smart way of solving this problem.
        Lets say if a is length 3. b is length 6. But if we traverse a+b or b+a, it will surely cover 9.
        With the same logic, we keep traversing and in the end we are sure to find the intersection node
        """
        curr_a, curr_b = headA, headB
        
        while curr_a!=curr_b:
            curr_a = curr_a.next if curr_a else headB
            curr_b = curr_b.next if curr_b else headA
        
        return curr_a
            