class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count, res = Counter(changed), []
        
        for num in sorted(changed):
            if count[num]==0: continue
            if count[2*num]==0: return []
            res.append(num)
            if num==0 and count[num]<=1: return []
            count[num]-=1
            count[num*2]-=1
            
        return res