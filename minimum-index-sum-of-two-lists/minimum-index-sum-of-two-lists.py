class Solution:
    def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:
        major, minor = (l2, l1) if len(l1)<len(l2) else (l1, l2)
        minor_map = {}
        for i, item in enumerate(minor): minor_map[item]=i
        
        res, min_val = [], float('inf')
        
        for i, item in enumerate(major):
            if item in minor_map:
                if minor_map[item]+i<min_val:
                    min_val = minor_map[item]+i
                    res = [item]
                elif minor_map[item]+i==min_val:
                    res.append(item)
        
        return res