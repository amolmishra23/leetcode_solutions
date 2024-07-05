# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical_indexes(node):
            localminima = lambda a, b, c: a and b and c and a.val<b.val and a.val<c.val
            localmaxima = lambda a, b, c: a and b and c and a.val>b.val and a.val>c.val
            prev, idx, critical = None, 0, []
            
            while node:
                if localminima(node, prev, node.next):
                    critical.append(idx)
                elif localmaxima(node, prev, node.next):
                    critical.append(idx)
                prev = node
                node = node.next
                idx += 1
                    
            return critical
        
        index = critical_indexes(head)
        if len(index)<=1: return [-1, -1]
        
        min_diff = min(b-a for a, b in zip(index[:-1], index[1:]))
        max_diff = index[-1]-index[0]
        return [min_diff, max_diff]