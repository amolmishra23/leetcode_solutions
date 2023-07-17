# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def size(head):
            res = 0 
            while head:
                res += 1
                head = head.next        
            return res
        
        s1, s2 = size(l1), size(l2)
        resHead, newNode = None, None
        
        while (l1 or l2):
            v1, v2 = 0, 0
            
            if (l1 and s1>=s2):
                v1 = l1.val
                l1 = l1.next
                s1 -= 1
            
            if (l2 and s2>=s1+1):
                v2 = l2.val
                l2 = l2.next
                s2 -= 1
                
            newNode=ListNode(v1+v2)
            newNode.next = resHead
            resHead = newNode
            
        print(resHead)
        carry = 0
        prev = None
        
        while resHead is not None:
            resHead.val += carry
            if resHead.val >= 10:
                resHead.val = resHead.val%10
                carry = 1
            else:
                carry = 0
            
            # lets reverse it again
            temp = resHead.next
            resHead.next = prev
            prev = resHead
            resHead = temp
            
        if carry>0:
            newNode = ListNode(1)
            newNode.next = prev
            prev = newNode
        
        return prev
            
        
        