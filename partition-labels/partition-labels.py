class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res, map_ = [], {}
        
        for i, char in enumerate(s):
            """
            Index of the last positions, where a particular character occurs. 
            """
            map_[char] = i
            
        left, right = 0, 0
        
        for i, char in enumerate(s):
            """
            Limiting ourselves to the max index that curr letter occurs. 
            If we are at end of such a streak, we instantly store the length in res.
            And increment the left pointer by 1 for the next iterations. 
            """
            right = max(right, map_[char])
            if right==i:
                res.append(right-left+1)
                left = right+1
        
        return res