class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = []
        
        for ppl, start, end in trips:
            l.append((start, ppl))
            l.append((end, -ppl))
            
        l.sort()
        
        for _, ppl in l:
            capacity -= ppl
            if capacity < 0: return False
            
        return True