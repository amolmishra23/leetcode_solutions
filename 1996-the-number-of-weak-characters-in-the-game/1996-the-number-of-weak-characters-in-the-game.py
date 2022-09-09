"""
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))
        stk = []
        
        for a,d in properties:
            while stk and stk[-1]<d: stk.pop()
            stk.append(d)
        
        return len(properties)-len(stk)
"""

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        weak, max_defence = 0, 0
        
        for a,d in properties[::-1]:
            if d<max_defence: weak+=1
            else: max_defence = max(max_defence, d)
        
        return weak
        